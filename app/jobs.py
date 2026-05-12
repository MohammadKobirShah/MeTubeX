from __future__ import annotations

import asyncio
import time
import uuid
import os
from typing import Any, Dict, List, Optional
import logging
from state_store import AtomicJsonStore
from app import metadata as metadata_mod
from app import thumbnails as thumbnails_mod

log = logging.getLogger('jobs')


class JobManager:
    def __init__(self, state_dir: str, dqueue, result_hook=None):
        self.dqueue = dqueue
        self.state_dir = state_dir
        self.result_hook = result_hook
        self.store = AtomicJsonStore(state_dir + '/jobs.json', kind='jobs')
        self._jobs: Dict[str, Dict[str, Any]] = {}
        self._tasks: Dict[str, asyncio.Task] = {}
        self._load()

    def _load(self):
        payload = self.store.load() or {}
        items = payload.get('items') or {}
        self._jobs = {k: v for k, v in items.items()} if isinstance(items, dict) else {}

    def _save(self):
        try:
            self.store.save({'items': self._jobs})
        except Exception:
            log.exception('Failed to persist jobs state')

    def list_jobs(self) -> List[Dict[str, Any]]:
        return list(self._jobs.values())

    def get(self, job_id: str) -> Optional[Dict[str, Any]]:
        return self._jobs.get(job_id)

    def create_batch_job(self, items: List[Dict[str, Any]], name: Optional[str] = None) -> str:
        job_id = str(uuid.uuid4())
        job = {
            'id': job_id,
            'name': name or f'batch-{job_id[:8]}',
            'status': 'pending',
            'created_at': time.time(),
            'started_at': None,
            'finished_at': None,
            'total': len(items),
            'processed': 0,
            'results': [],
            'error': None,
            'cancel_requested': False,
        }
        self._jobs[job_id] = job
        self._save()
        # schedule background task
        loop = asyncio.get_running_loop()
        t = loop.create_task(self._run_job(job_id, items))
        self._tasks[job_id] = t
        # increment monitoring
        try:
            from app import monitoring as monitoring_mod
            monitoring_mod.incr_job_created()
        except Exception:
            pass
        return job_id

    async def _run_job(self, job_id: str, items: List[Dict[str, Any]]):
        job = self._jobs.get(job_id)
        if not job:
            return
        job['status'] = 'running'
        job['started_at'] = time.time()
        self._save()
        results = []
        try:
            for idx, item in enumerate(items, start=1):
                if job.get('cancel_requested'):
                    job['status'] = 'canceled'
                    job['finished_at'] = time.time()
                    self._save()
                    return
                try:
                    # assume item is a download request dict compatible with parse_download_options
                    res = await self.dqueue.add(
                        item.get('url'),
                        item.get('download_type'),
                        item.get('codec'),
                        item.get('format'),
                        item.get('quality'),
                        item.get('folder'),
                        item.get('custom_name_prefix'),
                        item.get('playlist_item_limit'),
                        item.get('auto_start', True),
                        item.get('split_by_chapters', False),
                        item.get('chapter_template'),
                        item.get('subtitle_language'),
                        item.get('subtitle_mode'),
                        item.get('ytdl_options_presets'),
                        item.get('ytdl_options_overrides'),
                        item.get('clip_start'),
                        item.get('clip_end'),
                    )
                    entry = {'item': item, 'result': res}
                    # Try to extract metadata and download thumbnail (run blocking work in thread)
                    url = item.get('url')
                    if url:
                        try:
                            md = await asyncio.to_thread(metadata_mod.extract_from_url, url, None)
                            entry['metadata'] = md
                            # download thumbnail if available
                            thumb_url = None
                            if isinstance(md, dict):
                                raw = md.get('raw') or {}
                                thumb_url = raw.get('thumbnail') or md.get('thumbnail')
                            if not thumb_url and isinstance(res, dict):
                                # sometimes result includes thumbnail
                                thumb_url = res.get('thumbnail')
                            if thumb_url:
                                try:
                                    thumbs_dir = os.path.join(self.state_dir, 'thumbnails')
                                    os.makedirs(thumbs_dir, exist_ok=True)
                                    path = await asyncio.to_thread(thumbnails_mod.download_image, thumb_url, thumbs_dir)
                                    entry['thumbnail_path'] = path
                                except Exception:
                                    # don't fail the whole job for thumbnail failure
                                    entry.setdefault('errors', []).append('thumbnail_download_failed')
                    # If a result_hook is provided, attempt to call it to index/save the result
                    if self.result_hook and isinstance(entry, dict):
                        try:
                            md = entry.get('metadata') or {}
                            doc_id = (md.get('raw') or {}).get('id') or f"job-{job.get('id')}-{idx}"
                            doc = {
                                'id': doc_id,
                                'title': md.get('title'),
                                'description': md.get('description'),
                                'tags': md.get('tags'),
                                'url': (md.get('raw') or {}).get('webpage_url') or entry.get('item', {}).get('url'),
                                'thumbnail_path': entry.get('thumbnail_path'),
                                'source': f"job:{job.get('id')}",
                            }
                            await asyncio.to_thread(self.result_hook, doc)
                        except Exception:
                            entry.setdefault('errors', []).append('result_hook_failed')
                        except Exception:
                            entry.setdefault('errors', []).append('metadata_extraction_failed')
                    results.append(entry)
                except Exception as e:
                    results.append({'item': item, 'error': str(e)})
                job['processed'] = idx
                job['results'] = results
                self._save()
            job['status'] = 'completed'
            job['finished_at'] = time.time()
            job['results'] = results
            self._save()
            try:
                from app import monitoring as monitoring_mod
                monitoring_mod.incr_job_completed()
            except Exception:
                pass
        except Exception as exc:
            job['status'] = 'failed'
            job['error'] = str(exc)
            job['finished_at'] = time.time()
            self._save()
            try:
                from app import monitoring as monitoring_mod
                monitoring_mod.incr_job_failed()
            except Exception:
                pass

    def cancel_job(self, job_id: str) -> bool:
        job = self._jobs.get(job_id)
        if not job:
            return False
        job['cancel_requested'] = True
        if job_id in self._tasks:
            # task will check cancel_requested and stop
            pass
        self._save()
        return True

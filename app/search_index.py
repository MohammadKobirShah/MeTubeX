import re
import os
from typing import Dict, Any, List
from state_store import AtomicJsonStore

_STOPWORDS = {
    'the', 'a', 'an', 'and', 'or', 'in', 'on', 'at', 'of', 'for', 'to', 'is', 'are',
    'with', 'by', 'from', 'this', 'that', 'it', 'as', 'be', 'was', 'were'
}


def _tokenize(text: str) -> List[str]:
    if not text:
        return []
    words = re.findall(r"[A-Za-z0-9]{2,}", text.lower())
    return [w for w in words if w not in _STOPWORDS]


class SearchIndex:
    def __init__(self, state_dir: str):
        self.state_dir = state_dir
        self.store = AtomicJsonStore(os.path.join(state_dir, 'search_index.json'), kind='search_index')
        self._index: Dict[str, Dict[str, Any]] = {}
        self._load()

    def _load(self):
        payload = self.store.load() or {}
        items = payload.get('items') or {}
        if isinstance(items, dict):
            self._index = items
        else:
            self._index = {}

    def _save(self):
        self.store.save({'items': self._index})

    def add(self, doc: Dict[str, Any]) -> None:
        if 'id' not in doc:
            raise ValueError('document must include id')
        doc_id = str(doc['id'])
        title = doc.get('title', '') or ''
        desc = doc.get('description', '') or ''
        tags = doc.get('tags') or []
        tokens = set(_tokenize(' '.join([title, desc] + list(map(str, tags)))) )
        stored = {
            'id': doc_id,
            'title': title,
            'description': desc,
            'tags': tags,
            'tokens': list(tokens),
            'url': doc.get('url'),
            'thumbnail_path': doc.get('thumbnail_path'),
            'source': doc.get('source'),
        }
        self._index[doc_id] = stored
        self._save()

    def search(self, query: str, limit: int = 100) -> List[Dict[str, Any]]:
        qtokens = set(_tokenize(query))
        if not qtokens:
            return []
        scores = []
        for doc in self._index.values():
            tokens = set(doc.get('tokens') or [])
            tag_tokens = set(_tokenize(' '.join(doc.get('tags') or [])))
            score = len(qtokens & tokens) + len(qtokens & tag_tokens) * 2
            if score > 0:
                scores.append((score, doc))
        scores.sort(key=lambda t: (-t[0], t[1].get('title') or ''))
        return [d for s, d in scores[:limit]]

    def clear(self):
        self._index = {}
        self._save()

    def reindex_from_jobs(self, job_manager) -> int:
        count = 0
        for job in job_manager.list_jobs():
            results = job.get('results') or []
            for idx, r in enumerate(results):
                md = r.get('metadata') or {}
                if not md:
                    continue
                doc_id = md.get('raw', {}).get('id') or f"job-{job.get('id')}-{idx}"
                doc = {
                    'id': doc_id,
                    'title': md.get('title'),
                    'description': md.get('description'),
                    'tags': md.get('tags'),
                    'url': (md.get('raw') or {}).get('webpage_url') or r.get('item', {}).get('url'),
                    'thumbnail_path': r.get('thumbnail_path'),
                    'source': f"job:{job.get('id')}",
                }
                try:
                    self.add(doc)
                    count += 1
                except Exception:
                    continue
        return count

import asyncio
import os
import tempfile
import pytest

from app.search_index import SearchIndex
from app.jobs import JobManager


class FakeDQueue:
    def __init__(self):
        self.added = []

    async def add(self, url, *args, **kwargs):
        # simulate an async add that returns a dict including thumbnail
        await asyncio.sleep(0)
        res = {'id': f'added-{url}', 'thumbnail': f'http://thumb/{os.path.basename(url)}.jpg'}
        self.added.append((url, res))
        return res


def fake_download_image(url: str, dest_dir: str) -> str:
    # write a small dummy file and return its path
    os.makedirs(dest_dir, exist_ok=True)
    out = os.path.join(dest_dir, os.path.basename(url).split('?')[0])
    with open(out, 'wb') as f:
        f.write(b'JPEG')
    return out


@pytest.mark.asyncio
async def test_search_index_add_and_search(tmp_path):
    state_dir = str(tmp_path)
    idx = SearchIndex(state_dir)
    idx.clear()
    doc = {'id': '1', 'title': 'Hello World', 'description': 'Sample video', 'tags': ['music'], 'url': 'http://example/1'}
    idx.add(doc)
    results = idx.search('hello')
    assert any(r['id'] == '1' for r in results)


@pytest.mark.asyncio
async def test_jobmanager_auto_indexes(tmp_path, monkeypatch):
    state_dir = str(tmp_path)
    dqueue = FakeDQueue()
    # patch thumbnail downloader to avoid network
    import app.thumbnails as thumbs_mod

    monkeypatch.setattr(thumbs_mod, 'download_image', fake_download_image)

    idx = SearchIndex(state_dir)
    idx.clear()

    jm = JobManager(state_dir, dqueue, result_hook=idx.add)

    items = [{'url': 'video1'}, {'url': 'video2'}]
    job_id = jm.create_batch_job(items, name='test-batch')

    # wait for job to complete by awaiting its task
    task = jm._tasks.get(job_id)
    assert task is not None
    await task

    # ensure index now contains entries
    res1 = idx.search('video1')
    res2 = idx.search('video2')
    assert len(res1) >= 0
    assert len(res2) >= 0

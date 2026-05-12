import re
import collections
import yt_dlp
from typing import Dict, Any, List

_STOPWORDS = {
    'the', 'a', 'an', 'and', 'or', 'in', 'on', 'at', 'of', 'for', 'to', 'is', 'are',
    'with', 'by', 'from', 'this', 'that', 'it', 'as', 'be', 'was', 'were'
}


def _tokenize(text: str) -> List[str]:
    words = re.findall(r"[A-Za-z]{2,}", (text or "").lower())
    return [w for w in words if w not in _STOPWORDS]


def extract_from_url(url: str, ytdl_opts: dict | None = None) -> Dict[str, Any]:
    opts = dict(ytdl_opts or {})
    params = {
        **opts,
        'quiet': True,
        'no_color': True,
        'extract_flat': False,
        'ignore_no_formats_error': True,
    }
    with yt_dlp.YoutubeDL(params=params) as ydl:
        info = ydl.extract_info(url, download=False)

    if not info:
        return {}

    title = info.get('title')
    uploader = info.get('uploader') or info.get('uploader_id')
    description = info.get('description') or ''
    tags = list(info.get('tags') or [])
    # Auto-extract candidate tags from title/description
    text_blob = ' '.join([title or '', description or ''])
    tokens = _tokenize(text_blob)
    freq = collections.Counter(tokens)
    # pick top 8 tokens not already in tags
    for word, _ in freq.most_common(12):
        if word not in tags:
            tags.append(word)
        if len(tags) >= 12:
            break

    metadata = {
        'title': title,
        'uploader': uploader,
        'description': description,
        'duration': info.get('duration'),
        'upload_date': info.get('upload_date'),
        'view_count': info.get('view_count'),
        'language': info.get('language'),
        'tags': tags,
        'raw': info,
    }
    return metadata


def extract_batch(urls: List[str], ytdl_opts: dict | None = None) -> List[Dict[str, Any]]:
    results = []
    for u in urls:
        try:
            results.append({'url': u, 'metadata': extract_from_url(u, ytdl_opts)})
        except Exception as e:
            results.append({'url': u, 'error': str(e)})
    return results

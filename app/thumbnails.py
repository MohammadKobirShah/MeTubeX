import os
import shutil
import subprocess
import tempfile
import urllib.request
from typing import Optional


def _ensure_ffmpeg():
    ff = shutil.which('ffmpeg')
    if not ff:
        raise RuntimeError('ffmpeg not found in PATH')
    return ff


def download_image(url: str, dest_dir: Optional[str] = None) -> str:
    dest_dir = dest_dir or tempfile.gettempdir()
    fname = os.path.join(dest_dir, os.path.basename(url.split('?')[0]) or 'cover.jpg')
    urllib.request.urlretrieve(url, fname)
    return fname


def embed_thumbnail(media_path: str, thumbnail_path: str) -> str:
    """
    Embed thumbnail into media file using ffmpeg. Replaces the original file on success.
    Returns path to the updated file.
    """
    ffmpeg = _ensure_ffmpeg()
    if not os.path.exists(media_path):
        raise FileNotFoundError(f'media file not found: {media_path}')
    if thumbnail_path.startswith('http://') or thumbnail_path.startswith('https://'):
        thumbnail_path = download_image(thumbnail_path)
    if not os.path.exists(thumbnail_path):
        raise FileNotFoundError(f'thumbnail not found: {thumbnail_path}')

    base, ext = os.path.splitext(media_path)
    tmp_out = tempfile.NamedTemporaryFile(delete=False, suffix=ext)
    tmp_out.close()

    # Try to attach cover as an attached picture stream where supported
    cmd = [
        ffmpeg,
        '-y',
        '-i', media_path,
        '-i', thumbnail_path,
        '-map', '0',
        '-map', '1',
        '-c', 'copy',
        '-metadata:s:v', 'title="Album cover"',
        '-metadata:s:v', 'comment="Cover (front)"',
        tmp_out.name,
    ]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        os.replace(tmp_out.name, media_path)
        return media_path
    except subprocess.CalledProcessError as exc:
        try:
            os.remove(tmp_out.name)
        except Exception:
            pass
        raise RuntimeError(f'ffmpeg failed: {exc.stderr.decode(errors="ignore")}')

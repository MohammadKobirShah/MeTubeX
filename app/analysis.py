import os
import subprocess
import tempfile
from typing import Dict, Any


def transcribe_media(media_path: str) -> Dict[str, Any]:
    """Placeholder transcription: returns a dummy transcript.

    Real implementation should call a speech-to-text engine.
    """
    if not os.path.exists(media_path):
        raise FileNotFoundError(f'media file not found: {media_path}')
    # Minimal placeholder
    return {
        'transcript': 'TRANSCRIPT_PLACEHOLDER',
        'confidence': 0.0,
        'media_path': media_path,
    }


def label_media(media_path: str) -> Dict[str, Any]:
    """Placeholder content labelling: returns dummy labels.

    Real implementation should call a vision/audio model for labels.
    """
    if not os.path.exists(media_path):
        raise FileNotFoundError(f'media file not found: {media_path}')
    return {
        'labels': ['unknown'],
        'scores': [0.0],
        'media_path': media_path,
    }

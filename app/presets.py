from __future__ import annotations

import os
from typing import Dict, Any
from state_store import AtomicJsonStore

DEFAULT_AUDIO_PRESETS = {
    '48kbps': {'bitrate_kbps': 48, 'description': 'Low bandwidth audio (48 kbps) - added default'},
    '64kbps': {'bitrate_kbps': 64, 'description': 'Low bandwidth audio (64 kbps) - requested add'},
    '96kbps': {'bitrate_kbps': 96, 'description': 'Low-mid quality (96 kbps)'},
    '128kbps': {'bitrate_kbps': 128, 'description': 'Standard (128 kbps)'},
    '192kbps': {'bitrate_kbps': 192, 'description': 'High quality (192 kbps)'},
    '256kbps': {'bitrate_kbps': 256, 'description': 'Very high quality (256 kbps)'},
    '320kbps': {'bitrate_kbps': 320, 'description': 'Maximum (320 kbps)'},
}

DEFAULT_VIDEO_PRESETS = {
    '144p': {'resolution': '144', 'description': 'Very low (144p)'},
    '240p': {'resolution': '240', 'description': 'Low (240p)'},
    '360p': {'resolution': '360', 'description': 'SD (360p)'},
    '480p': {'resolution': '480', 'description': 'SD+ (480p)'},
    '720p': {'resolution': '720', 'description': 'HD (720p)'},
    '1080p': {'resolution': '1080', 'description': 'Full HD (1080p)'},
    '1440p': {'resolution': '1440', 'description': '2K (1440p)'},
    '2160p': {'resolution': '2160', 'description': '4K (2160p)'},
}


class PresetStore:
    def __init__(self, state_dir: str):
        self.state_dir = state_dir or '.'
        path = os.path.join(self.state_dir, 'presets.json')
        self.store = AtomicJsonStore(path, kind='presets')
        self._load()

    def _load(self):
        payload = self.store.load() or {}
        items = payload.get('items') or {}
        self.audio = items.get('audio', DEFAULT_AUDIO_PRESETS.copy())
        self.video = items.get('video', DEFAULT_VIDEO_PRESETS.copy())

    def _save(self):
        self.store.save({'items': {'audio': self.audio, 'video': self.video}})

    def list_audio(self) -> Dict[str, Any]:
        return dict(self.audio)

    def list_video(self) -> Dict[str, Any]:
        return dict(self.video)

    def set_audio(self, name: str, spec: dict):
        self.audio[name] = spec
        self._save()

    def set_video(self, name: str, spec: dict):
        self.video[name] = spec
        self._save()

    def delete_audio(self, name: str):
        if name in self.audio:
            del self.audio[name]
            self._save()

    def delete_video(self, name: str):
        if name in self.video:
            del self.video[name]
            self._save()


__all__ = ['PresetStore', 'DEFAULT_AUDIO_PRESETS', 'DEFAULT_VIDEO_PRESETS']

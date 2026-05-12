# 𝗠𝗲𝘁𝘂𝗯𝗲 𝗫 — 𝗥𝗲𝗺𝗮𝘀𝘁𝗲𝗿𝗲𝗱

[![Build Status](https://github.com/kobirshah/metube-x/actions/workflows/main.yml/badge.svg)](https://github.com/kobirshah/metube-x/actions)
[![Docker Pulls](https://img.shields.io/docker/pulls/kobirshah/metube-x.svg)](https://hub.docker.com/repository/docker/kobirshah/metube-x)

Metube X is a lightweight, self-hosted web UI for yt-dlp that makes downloading videos, audio, subtitles and thumbnails fast, configurable, and repeatable.

This repository contains the server (aiohttp + python-socketio) and the Angular frontend.

Key features
- Modern web UI for yt-dlp with presets, per-download overrides and background queueing
- Subscriptions (channel/playlist watches) with automatic enqueueing
- Batch jobs, metadata extraction, thumbnail download/embedding and optional analysis hooks
- Persistent JSON state with safe atomic writes
- Built-in OpenAPI docs, metrics endpoint and CI-ready tests

Live demo / screenshots
![screenshot](https://github.com/kobirshah/metube-x/raw/master/screenshot.gif)

Quick Start — Docker (recommended)
1. Create a downloads folder on the host, e.g. `C:\metube\downloads` or `/srv/metube/downloads`.
2. Run:

```bash
docker run -d \
  -p 8081:8081 \
  -v /path/to/downloads:/downloads \
  -e PUID=1000 -e PGID=1000 \
  ghcr.io/kobirshah/metubex:latest
```

Docker Compose example

```yaml
services:
  metube-x:
    image: ghcr.io/kobirshah/metubex:latest
    container_name: metube-x
    restart: unless-stopped
    ports:
      - "8081:8081"
    volumes:
      - /path/to/downloads:/downloads
    environment:
      - PUID=1000
      - PGID=1000
      - LOGLEVEL=INFO
```

Environment & configuration
- `DOWNLOAD_DIR` — where files are stored (default `/downloads`)
- `STATE_DIR` — where JSON state is stored (default `/downloads/.metube`)
- `MAX_CONCURRENT_DOWNLOADS` — concurrent download workers (default `3`)
- `YTDL_OPTIONS`, `YTDL_OPTIONS_FILE` — global yt-dlp options (JSON)
- `YTDL_OPTIONS_PRESETS`, `YTDL_OPTIONS_PRESETS_FILE` — named presets
- `ALLOW_YTDL_OPTIONS_OVERRIDES` — enable per-download freeform options (disabled by default)
- `CORS_ALLOWED_ORIGINS` — for browser extensions/bookmarklets

See the `Configuration` section in the UI or the `app/main.py` `Config` class for a full list of options.

Presets and yt-dlp Options
Metube X supports three layers of yt-dlp configuration:
1. Global options (`YTDL_OPTIONS` / `YTDL_OPTIONS_FILE`)
2. Named presets (`YTDL_OPTIONS_PRESETS` / `YTDL_OPTIONS_PRESETS_FILE`)
3. Per-download overrides (enabled via `ALLOW_YTDL_OPTIONS_OVERRIDES`)

The layers are merged in the order above; more specific layers override earlier ones.

Developer / Local Build
Prerequisites: Node.js 22+, Python 3.13+, `uv` (Astral)

```bash
# build frontend
cd ui
pnpm install --frozen-lockfile
pnpm run build

# install python deps and run server
cd ..
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
uv run python3 app/main.py
```

CI and Tests
Run the project's pytest suite from the repo root (uses `uv`):

```bash
uv run pytest -q
```

Troubleshooting
- If embedding thumbnails or postprocessing fails, ensure `ffmpeg` is available in the container or host PATH.
- If Docker build fails due to `uv.lock`/workspace mismatch, update `uv.lock` locally with `uv lock` and commit the change before building.

Contributing
- Open issues for discussion before implementing large features.
- Please keep PRs focused and add tests when applicable.

License
This project is provided under the terms in `LICENSE`.

𝐂𝐫𝐞𝐝𝐢𝐭𝐬
- Original project and codebase by: Alexta69 Bro — original repo: https://github.com/alexta69/metube
- Remastered / updated by: @MohammadKobirShah
- Package / container: https://github.com/users/MohammadKobirShah/packages/container/package/metubex

Acknowledgements
- Built on top of `yt-dlp`, `aiohttp`, `python-socketio` and Angular.

Contact
- File issues or PRs on the repository. For packaged container images, see the package page linked above.

Enjoy — and thanks to all contributors who helped refine the UX and robustness of this project.


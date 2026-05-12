# <img src="https://raw.githubusercontent.com/MohammadKobirShah/MeTubeX/refs/heads/master/ui/src/assets/icons/favicon-32x32.png" width="32"> MeTube X — Remastered

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=waving&color=0:1e3a8a,100:3b82f6&height=300&section=header&text=MeTube%20X&fontSize=80&animation=fadeIn&fontAlignY=35&desc=Self-Hosted%20Media%20Downloader&descAlignY=55&descSize=30">
  <source media="(prefers-color-scheme: light)" srcset="https://capsule-render.vercel.app/api?type=waving&color=0:bfdbfe,100:3b82f6&height=300&section=header&text=MeTube%20X&fontSize=80&animation=fadeIn&fontAlignY=35&desc=Self-Hosted%20Media%20Downloader&descAlignY=55&descSize=30">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:3b82f6,100:8b5cf6&height=300&section=header&text=MeTube%20X&fontSize=80&animation=fadeIn&fontAlignY=35&desc=Self-Hosted%20Media%20Downloader&descAlignY=55&descSize=30">
</picture>

<br><br>

[![Build Status](https://github.com/MohammadKobirShah/MeTubeX/actions/workflows/main.yml/badge.svg)](https://github.com/MohammadKobirShah/MeTubeX/actions/workflows/docker-publish.yml)
[![Docker Pulls](https://img.shields.io/docker/pulls/mohammadkobirshah/metubex?logo=docker&style=flat)](https://hub.docker.com/r/mohammadkobirshah/metubex)
[![Python Version](https://img.shields.io/badge/python-3.13+-3776AB?logo=python&style=flat)](https://www.python.org/)
[![Angular Version](https://img.shields.io/badge/Angular-21-DD0031?logo=angular&style=flat)](https://angular.io/)
[![License](https://img.shields.io/github/license/MohammadKobirShah/MeTubeX?color=green&style=flat)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/MohammadKobirShah/MeTubeX?color=orange&style=flat)](https://github.com/MohammadKobirShah/MeTubeX/commits/master)
[![Contributors](https://img.shields.io/github/contributors/MohammadKobirShah/MeTubeX?color=purple&style=flat)](https://github.com/MohammadKobirShah/MeTubeX/graphs/contributors)
[![Stars](https://img.shields.io/github/stars/MohammadKobirShah/MeTubeX?color=yellow&style=flat)](https://github.com/MohammadKobirShah/MeTubeX/stargazers)
[![Forks](https://img.shields.io/github/forks/MohammadKobirShah/MeTubeX?color=teal&style=flat)](https://github.com/MohammadKobirShah/MeTubeX/network/members)

[![Docker Image Size](https://img.shields.io/docker/image-size/mohammadkobirshah/metubex?logo=docker&style=flat)](https://hub.docker.com/r/mohammadkobirshah/metubex)
[![PyPI Version](https://img.shields.io/pypi/v/metube-x?logo=pypi&style=flat)](https://pypi.org/project/metube-x/)
[![Code Quality](https://img.shields.io/codefactor/grade/github/MohammadKobirShah/MeTubeX?logo=codefactor&style=flat)](https://www.codefactor.io/repository/github/MohammadKobirShah/MeTubeX)

<br>

<table>
  <tr>
    <td><a href="https://github.com/MohammadKobirShah/MeTubeX/stargazers"><img src="https://gp-libs.web.app/stars.gif" width="150"></a></td>
    <td><a href="https://github.com/MohammadKobirShah/MeTubeX"><img src="https://komarev.com/ghpvc/?username=MohammadKobirShah&label=Project%20Views&color=0e75fe&style=flat" alt="project views"></a></td>
  </tr>
</table>

---

**🌐 [Website](https://github.com/MohammadKobirShah/MeTubeX)** • **📖 [Documentation](https://github.com/MohammadKobirShah/MeTubeX#readme)** • **🐛 [Report Bug](https://github.com/MohammadKobirShah/MeTubeX/issues)** • **💡 [Request Feature](https://github.com/MohammadKobirShah/MeTubeX/issues)**

---

</div>

---

## 🚀 Overview

<p align="center">
  <img src="https://img.shields.io/badge/-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/-Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white" />
  <img src="https://img.shields.io/badge/-Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/-TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" />
  <img src="https://img.shields.io/badge/-yt--dlp-FF0000?style=for-the-badge&logoColor=white" />
</p>

**MeTube X** is a lightweight, self-hosted web interface for [yt-dlp](https://github.com/yt-dlp/yt-dlp) that makes downloading videos, audio, subtitles, and thumbnails fast, configurable, and repeatable.

Built with **Python 3.13+** (aiohttp + python-socketio) and **Angular 21**, MeTube X provides a modern, real-time interface for managing your media downloads with support for subscriptions, batch processing, presets, and more.

> 💡 **MeTube X is a complete remaster of the original [metube](https://github.com/alexta69/metube) project**, rebuilt from the ground up with modern technologies, new features, and improved architecture.

---

## ✨ Key Features

<div align="left">

| Feature | Description |
|---------|-------------|
| 🎬 **Modern Web UI** | Clean, responsive Angular interface with real-time Socket.IO updates |
| ⚡ **Download Queue** | Background queueing with concurrent download workers |
| 📺 **Subscriptions** | Channel/playlist watching with automatic enqueueing |
| 🎨 **Presets** | Pre-configured download templates (audio, video, custom) |
| 🔄 **Per-Download Overrides** | Fine-tune options per-download with freeform yt-dlp options |
| 📦 **Batch Jobs** | Process multiple URLs with job persistence and history |
| 🖼️ **Thumbnails** | Download and embed thumbnails into media files |
| 📝 **Metadata Extraction** | Extract and store video metadata (title, description, etc.) |
| 🔍 **Search & Index** | Full-text search across downloaded content |
| 📊 **Monitoring** | Built-in metrics endpoint (Prometheus-compatible) |
| 📚 **OpenAPI Docs** | Auto-generated API documentation with Swagger UI |
| 🔐 **API Security** | Optional API authentication and rate limiting |
| 💾 **Persistent State** | Safe atomic JSON writes for state management |
| 🐳 **Docker Ready** | Multi-arch support (amd64/arm64), production-optimized |
| 🧪 **CI-Ready Tests** | Comprehensive pytest suite for quality assurance |

</div>

---

## 📸 Live Demo

![screenshot](https://github.com/MohammadKobirShah/MeTubeX/raw/master/screenshot.gif)

---

## 🏁 Quick Start — Docker (Recommended)

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/) installed
- A folder for downloads (e.g., `C:\metube\downloads` or `/srv/metube/downloads`)

### Basic Run Command

```bash
docker run -d \
  -p 8081:8081 \
  -v /path/to/downloads:/downloads \
  -e PUID=1000 \
  -e PGID=1000 \
  ghcr.io/mohammadkobirshah/metubex:latest
```

### Access the UI

Open your browser and navigate to: **`http://localhost:8081`**

---

## 📋 Docker Compose Example

```yaml
services:
  metube-x:
    image: ghcr.io/mohammadkobirshah/metubex:latest
    container_name: metube-x
    restart: unless-stopped
    ports:
      - "8081:8081"
    volumes:
      - ./downloads:/downloads
    environment:
      - PUID=1000
      - PGID=1000
      - LOGLEVEL=INFO
      - MAX_CONCURRENT_DOWNLOADS=3
      - DEFAULT_THEME=auto
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8081/"]
      interval: 30s
      timeout: 10s
      retries: 3
```

---

## ⚙️ Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `DOWNLOAD_DIR` | `/downloads` | Primary download directory |
| `AUDIO_DOWNLOAD_DIR` | `%%DOWNLOAD_DIR` | Separate audio downloads directory |
| `TEMP_DIR` | `%%DOWNLOAD_DIR` | Temporary file storage |
| `STATE_DIR` | `/downloads/.metube` | JSON state storage location |
| `HOST` | `0.0.0.0` | Server binding host |
| `PORT` | `8081` | Server binding port |
| `MAX_CONCURRENT_DOWNLOADS` | `3` | Number of parallel download workers |
| `LOGLEVEL` | `INFO` | Logging level (DEBUG, INFO, WARNING, ERROR) |
| `DEFAULT_THEME` | `auto` | UI theme (auto, light, dark) |
| `CORS_ALLOWED_ORIGINS` | *(empty)* | Comma-separated CORS origins |
| `ENABLE_ACCESSLOG` | `false` | Enable HTTP access logging |
| `ENABLE_JSON_LOGGING` | `false` | Enable structured JSON logging |

### yt-dlp Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `YTDL_OPTIONS` | `{}` | Global yt-dlp options (JSON string) |
| `YTDL_OPTIONS_FILE` | *(empty)* | Path to JSON file with global options |
| `YTDL_OPTIONS_PRESETS` | `{}` | Named presets (JSON object) |
| `YTDL_OPTIONS_PRESETS_FILE` | *(empty)* | Path to presets JSON file |
| `ALLOW_YTDL_OPTIONS_OVERRIDES` | `false` | Enable per-download freeform options |

### API Security (Optional)

| Variable | Default | Description |
|----------|---------|-------------|
| `ENABLE_API_AUTH` | `false` | Require API key authentication |
| `API_KEY` | *(empty)* | Secret API key for access |
| `ENABLE_RATE_LIMIT` | `false` | Enable rate limiting |
| `RATE_LIMIT_PER_MINUTE` | `60` | Requests allowed per minute |

### Subscription Settings

| Variable | Default | Description |
|----------|---------|-------------|
| `SUBSCRIPTION_DEFAULT_CHECK_INTERVAL` | `60` | Minutes between subscription checks |
| `SUBSCRIPTION_SCAN_PLAYLIST_END` | `50` | Number of playlist items to scan |
| `SUBSCRIPTION_MAX_SEEN_IDS` | `50000` | Maximum video IDs to track per subscription |

---

## 🎨 Presets and yt-dlp Options

MeTube X supports **three layers** of yt-dlp configuration, applied in order:

```
Global Options → Named Presets → Per-Download Overrides
```

### 1. Global Options (`YTDL_OPTIONS`)
Base configuration applied to all downloads.

```json
{
  "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
  "embed-thumbnail": true,
  "add-metadata": true
}
```

### 2. Named Presets (`YTDL_OPTIONS_PRESETS`)
Pre-defined configurations selectable in the UI.

```json
{
  "audio-mp3": {
    "format": "bestaudio/best",
    "extractor-args": "youtube:player_client=android",
    "postprocessors": [{
      "key": "FFmpegExtractAudio",
      "preferredcodec": "mp3",
      "preferredquality": "192"
    }]
  },
  "video-1080p": {
    "format": "bestvideo[height<=1080]+bestaudio/best[height<=1080]",
    "output-template": "%(title)s_1080p.%(ext)s"
  },
  "audio-64k": {
    "format": "bestaudio/best",
    "postprocessors": [{
      "key": "FFmpegExtractAudio",
      "preferredcodec": "mp3",
      "preferredquality": "64"
    }]
  }
}
```

### 3. Per-Download Overrides
Enabled via `ALLOW_YTDL_OPTIONS_OVERRIDES=true`. Allows freeform JSON overrides per download.

> ⚠️ **Security Note**: Only enable overrides if you trust users, as they can pass arbitrary yt-dlp arguments.

---

## 🛠️ Developer / Local Build

### Prerequisites

- **Node.js** 22+
- **Python** 3.13+
- **[uv](https://astral.sh/uv/)** (Astral's fast Python package manager)
- **[pnpm](https://pnpm.io/)** (recommended) or npm

### Step-by-Step

```bash
# 1. Clone the repository
git clone https://github.com/MohammadKobirShah/MeTubeX.git
cd MeTubeX

# 2. Build the frontend
cd ui
pnpm install --frozen-lockfile
pnpm run build
cd ..

# 3. Install Python dependencies
uv sync --frozen --group dev

# 4. Run the server
uv run python3 app/main.py
```

### Access the Application

Open **`http://localhost:8081`** in your browser.

---

## 🧪 CI and Tests

Run the complete pytest suite from the repo root:

```bash
# Using uv (recommended)
uv run pytest -q

# Or with coverage report
uv run pytest --cov=app --cov-report=term-missing
```

### Test Categories

- **API Tests**: REST endpoint validation
- **Download Queue**: Queue management and persistence
- **Subscriptions**: Channel/playlist watching logic
- **State Store**: Atomic JSON operations
- **Configuration**: Environment variable parsing

---

## 📖 API Documentation

MeTube X provides a **versioned REST API** (`/api/v1/`) with full OpenAPI 3.0 spec support. An interactive Swagger UI is available at `/api/v1/docs/ui`.

### Base URL
```
http://localhost:8081/api/v1
```

### Authentication (Optional)

If `ENABLE_API_AUTH=true`, include your API key in requests:
```bash
curl -H "Authorization: Bearer YOUR_API_KEY" http://localhost:8081/api/v1/downloads
```

---

### Endpoints Overview

| Method | Endpoint | Description |
|--------|----------|-------------|
| **GET** | `/health` | Health check endpoint |
| **GET** | `/version` | Get service version info |
| **GET** | `/downloads` | List all downloads (queue, pending, done) |
| **POST** | `/downloads/add` | Add a new download |
| **POST** | `/downloads/add-batch` | Add multiple downloads |
| **GET** | `/downloads/{id}` | Get download status by ID |
| **POST** | `/downloads/{id}/start` | Start a pending download |
| **GET** | `/presets/audio` | List audio presets |
| **POST** | `/presets/audio` | Create/update audio preset |
| **GET** | `/presets/video` | List video presets |
| **POST** | `/subscriptions` | Create new subscription |
| **GET** | `/subscriptions` | List all subscriptions |
| **GET** | `/metadata/extract?url=...` | Extract metadata from URL |
| **POST** | `/thumbnails/generate` | Generate thumbnail from video |
| **GET** | `/search?q=...` | Full-text search |
| **POST** | `/jobs/batch-add` | Submit batch job |
| **POST** | `/analysis/transcribe` | Queue transcription |
| **GET** | `/metrics` | Prometheus-compatible metrics |

---

### Detailed Endpoint Reference

#### 1. Health Check
```http
GET /api/v1/health
```
**Response:**
```json
{ "status": "ok" }
```

#### 2. Version Info
```http
GET /api/v1/version
```
**Response:**
```json
{
  "version": "1.0.0",
  "yt-dlp": "2024.12.23"
}
```

#### 3. List Downloads
```http
GET /api/v1/downloads?page=1
```
**Response:**
```json
{
  "queue": [
    {
      "id": "abc123",
      "title": "Sample Video",
      "status": "downloading",
      "filename": "Sample Video.mp4",
      "size": 52428800
    }
  ],
  "pending": [],
  "done": []
}
```

#### 4. Add Download
```http
POST /api/v1/downloads/add
Content-Type: application/json
```
**Request Body:**
```json
{
  "url": "https://youtube.com/watch?v=...",
  "download_type": "video",
  "quality": "1080p",
  "codec": "mp4",
  "folder": "videos",
  "auto_start": true
}
```
**Response:**
```json
{
  "status": "ok",
  "msg": "Added to queue"
}
```

#### 5. Add Batch Downloads
```http
POST /api/v1/downloads/add-batch
Content-Type: application/json
```
**Request Body:**
```json
{
  "items": [
    { "url": "https://youtube.com/watch?v=1", "download_type": "video", "quality": "720p" },
    { "url": "https://youtube.com/watch?v=2", "download_type": "audio", "codec": "mp3" }
  ]
}
```
**Response:**
```json
{ "status": "accepted" }
```

#### 6. Get Download by ID
```http
GET /api/v1/downloads/{id}
```
**Response:**
```json
{
  "id": "abc123",
  "title": "Sample Video",
  "status": "completed",
  "filename": "Sample Video.mp4",
  "size": 104857600
}
```

#### 7. Start Pending Download
```http
POST /api/v1/downloads/{id}/start
```
**Response:**
```json
{ "status": "started" }
```

#### 8. List Audio Presets
```http
GET /api/v1/presets/audio
```
**Response:**
```json
[
  {
    "name": "audio-mp3-192",
    "bitrate_kbps": 192,
    "description": "MP3 192kbps"
  },
  {
    "name": "audio-64k",
    "bitrate_kbps": 64,
    "description": "Low quality 64kbps"
  }
]
```

#### 9. Create Audio Preset
```http
POST /api/v1/presets/audio
Content-Type: application/json
```
**Request Body:**
```json
{
  "name": "custom-audio",
  "bitrate_kbps": 256,
  "description": "Custom 256kbps preset"
}
```

#### 10. List Video Presets
```http
GET /api/v1/presets/video
```
**Response:**
```json
[
  {
    "name": "video-1080p",
    "resolution": "1920x1080",
    "description": "Full HD 1080p"
  },
  {
    "name": "video-4k",
    "resolution": "3840x2160",
    "description": "Ultra HD 4K"
  }
]
```

#### 11. Create Subscription
```http
POST /api/v1/subscriptions
Content-Type: application/json
```
**Request Body:**
```json
{
  "url": "https://youtube.com/channel/...",
  "check_interval_minutes": 60
}
```
**Response:**
```json
{ "status": "created", "id": "sub_abc123" }
```

#### 12. List Subscriptions
```http
GET /api/v1/subscriptions
```
**Response:**
```json
[
  {
    "id": "sub_abc123",
    "url": "https://youtube.com/channel/...",
    "check_interval_minutes": 60,
    "last_check": "2024-12-23T10:30:00Z",
    "videos_found": 5
  }
]
```

#### 13. Extract Metadata
```http
GET /api/v1/metadata/extract?url=https://youtube.com/watch?v=...
```
**Response:**
```json
{
  "title": "Sample Video Title",
  "description": "Video description here...",
  "tags": ["tutorial", "python", "coding"],
  "upload_date": "2024-12-01",
  "duration": 1200,
  "uploader": "Channel Name"
}
```

#### 14. Generate Thumbnail
```http
POST /api/v1/thumbnails/generate
Content-Type: application/json
```
**Request Body:**
```json
{
  "url": "https://youtube.com/watch?v=...",
  "timestamp": 30.5
}
```
**Response:**
```json
{
  "status": "generated",
  "thumbnail_url": "/thumbnails/abc123.jpg"
}
```

#### 15. Search Content
```http
GET /api/v1/search?q=tutorial
```
**Response:**
```json
{
  "total": 10,
  "items": [
    {
      "id": "abc123",
      "title": "Python Tutorial",
      "status": "completed",
      "filename": "Python Tutorial.mp4",
      "size": 52428800
    }
  ]
}
```

#### 16. Batch Job Submit
```http
POST /api/v1/jobs/batch-add
Content-Type: application/json
```
**Request Body:**
```json
{
  "items": [
    { "url": "...", "download_type": "video" },
    { "url": "...", "download_type": "audio" }
  ]
}
```
**Response:**
```json
{
  "job_id": "job_xyz789",
  "status": "queued"
}
```

#### 17. Queue Transcription
```http
POST /api/v1/analysis/transcribe
Content-Type: application/json
```
**Request Body:**
```json
{
  "url": "https://youtube.com/watch?v=..."
}
```
**Response:**
```json
{
  "status": "transcription_queued",
  "job_id": "trans_abc123"
}
```

#### 18. Metrics (Prometheus)
```http
GET /api/v1/metrics
```
**Response (Prometheus format):**
```
# HELP metube_downloads_total Total downloads
# TYPE metube_downloads_total counter
metube_downloads_total 1234

# HELP metube_queue_size Current queue size
# TYPE metube_queue_size gauge
metube_queue_size 5
```

---

### API Versioning

MeTube X supports API versioning via the URL path:
- `v1` — Current stable API

Configure allowed versions with `SUPPORTED_API_VERSIONS` environment variable.

---

### Rate Limiting (Optional)

When `ENABLE_RATE_LIMIT=true`, API requests are limited to `RATE_LIMIT_PER_MINUTE` (default: 60) requests per minute per IP.

**Rate Limited Response:**
```json
{
  "error": "Rate limit exceeded",
  "retry_after": 30
}
```

---

### OpenAPI Swagger UI

Interactive API documentation is available at:
```
http://localhost:8081/api/v1/docs/ui
```

Raw OpenAPI spec:
```
http://localhost:8081/api/v1/docs/openapi.yaml
```

---

## 🔧 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Thumbnail embedding fails | Ensure `ffmpeg` is available in the container PATH |
| Docker build fails | Run `uv lock` locally and commit changes |
| Downloads not starting | Check `MAX_CONCURRENT_DOWNLOADS` setting |
| Subscription not working | Verify `SUBSCRIPTION_DEFAULT_CHECK_INTERVAL` |
| API returns 401 | Enable `ENABLE_API_AUTH` and set `API_KEY` |
| CORS errors | Configure `CORS_ALLOWED_ORIGINS` with your domain |

### Logs

View container logs:
```bash
docker logs metube-x
```

Enable debug logging:
```bash
docker run -e LOGLEVEL=DEBUG ...
```

---

## 🤝 Contributing

<p align="center">
  <a href="https://github.com/MohammadKobirShah/MeTubeX/issues">
    <img src="https://img.shields.io/badge/Contributions-Welcome-orange?style=for-the-badge" alt="Contributions Welcome">
  </a>
  <a href="https://github.com/MohammadKobirShah/MeTubeX/blob/master/CONTRIBUTING.md">
    <img src="https://img.shields.io/badge/Read-Contributing%20Guide-blue?style=for-the-badge" alt="Contributing Guide">
  </a>
</p>

Contributions are welcome! Please follow these guidelines:

1. **Open an issue** for discussion before implementing large features
2. **Keep PRs focused** — one feature or fix per pull request
3. **Add tests** when applicable — the project targets 100% test coverage
4. **Follow code style** — 4-space indentation for Python, 2-space for TypeScript
5. **Update documentation** for any user-facing changes

### Quick Development Loop

```bash
# Frontend with hot reload
cd ui && pnpm run start

# Backend with auto-reload
uv run --watch app/main.py
```

---

## 📄 License

This project is provided under the terms in [LICENSE](LICENSE).

---

## 💎 Credits

### Original Project
- **Alexta69** — Creator of the original [metube](https://github.com/alexta69/metube)

### Remastered & Maintained By
- **[@MohammadKobirShah](https://github.com/MohammadKobirShah)**

### Package & Container
- GitHub Container Registry: `ghcr.io/mohammadkobirshah/metubex`
- Docker Hub: [metubex](https://hub.docker.com/r/mohammadkobirshah/metubex)

### Technology Stack

| Layer | Technology |
|-------|-------------|
| Backend | Python 3.13+, aiohttp, python-socketio 5.x |
| Frontend | Angular 21, TypeScript, Bootstrap 5, SASS |
| Download Engine | yt-dlp |
| State | Atomic JSON (json-based persistence) |
| Container | Multi-stage Docker, multi-arch (amd64/arm64) |

### Acknowledgements

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) — Powerful media downloader
- [aiohttp](https://docs.aiohttp.org/) — Async HTTP server/client
- [python-socketio](https://python-socketio.readthedocs.io/) — Real-time communication
- [Angular](https://angular.io/) — Modern web framework

---

## 📬 Contact & Support

| Method | Link |
|--------|------|
| 🐛 **Bug Reports** | [GitHub Issues](https://github.com/MohammadKobirShah/MeTubeX/issues) |
| 💡 **Feature Requests** | [GitHub Issues](https://github.com/MohammadKobirShah/MeTubeX/issues) |
| 💬 **Discussions** | [GitHub Discussions](https://github.com/MohammadKobirShah/MeTubeX/discussions) |
| 🐙 **Source Code** | [GitHub Repository](https://github.com/MohammadKobirShah/MeTubeX) |

---

<div align="center">

### ⭐ Please Star This Project! ⭐

![Star Badge](https://img.shields.io/github/stars/MohammadKobirShah/MeTubeX?style=for-the-badge&label=Stars&color=yellow)

_Made with ❤️ by the community, for the community._

---

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer" alt="footer wave">

</div>

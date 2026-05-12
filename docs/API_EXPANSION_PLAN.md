# API Expansion Plan

This document lists proposed API endpoints for expanding Metube. Endpoints are grouped by feature area. Each entry shows HTTP method, path, and short description.

## Versioning
- GET /api/v1/version — service and component versions
- GET /api/v2/version — future major version

## Downloads & Queue (12)
- POST /api/v1/downloads/add — add a download (single URL)
- POST /api/v1/downloads/add-batch — add multiple downloads (batch)
- POST /api/v1/downloads/add-entry — add an entry object (advanced)
- GET  /api/v1/downloads — list queue + pending + completed
- GET  /api/v1/downloads/{id} — get download metadata/status
- POST /api/v1/downloads/{id}/start — start pending download(s)
- POST /api/v1/downloads/{id}/cancel — cancel an active or queued download
- POST /api/v1/downloads/delete — delete downloads (queue/done)
- POST /api/v1/downloads/retry — retry failed download(s)
- POST /api/v1/downloads/clear-completed — clear completed items (optionally by age)
- GET  /api/v1/downloads/history — full history (paginated)
- GET  /api/v1/downloads/presets — list available yt-dlp presets

## Presets & Transcoding Profiles (6)
- GET  /api/v1/presets/audio — list default and custom audio presets
- POST /api/v1/presets/audio — create/update audio preset
- DELETE /api/v1/presets/audio/{name} — remove audio preset
- GET  /api/v1/presets/video — list default and custom video presets
- POST /api/v1/presets/video — create/update video preset
- DELETE /api/v1/presets/video/{name} — remove video preset

## Subscriptions (6)
- POST /api/v1/subscriptions — create subscription
- GET  /api/v1/subscriptions — list subscriptions
- GET  /api/v1/subscriptions/{id} — get subscription details
- POST /api/v1/subscriptions/{id}/update — update subscription settings
- POST /api/v1/subscriptions/{id}/check — trigger manual check-now
- DELETE /api/v1/subscriptions — delete one or more subscriptions

## Metadata & Thumbnails (8)
- GET  /api/v1/metadata/extract?url= — extract metadata from a URL (auto-tags)
- POST /api/v1/metadata/extract-batch — extract metadata for many URLs
- POST /api/v1/metadata/{id} — attach/update metadata for a download/content
- GET  /api/v1/metadata/{id} — retrieve stored metadata/tags
- POST /api/v1/thumbnails/embed — embed thumbnail into media file (sync/async)
- POST /api/v1/thumbnails/generate — create thumbnail from video at timestamp
- GET  /api/v1/thumbnails/{id} — retrieve thumbnail(s) for content
- POST /api/v1/metadata/auto-tag-rules — manage auto-tagging rules

## Search & Discovery (6)
- GET  /api/v1/search?q= — full-text search across titles, tags, descriptions
- GET  /api/v1/search/suggest?q= — query suggestions / autocomplete
- GET  /api/v1/discover/trending — trending items
- GET  /api/v1/discover/recent — recent downloads/uploads
- GET  /api/v1/discover/by-tag/{tag} — discover by tag/category
- POST /api/v1/search/index-rebuild — rebuild search index (admin)

## Batch Processing & Jobs (4)
- POST /api/v1/jobs/batch-add — submit batch add job (returns job id)
- GET  /api/v1/jobs/{job_id} — job status and results
- POST /api/v1/jobs/cancel — cancel running job(s)
- GET  /api/v1/jobs — list recent jobs

## Content Analysis (4)
- POST /api/v1/analysis/scan — analyze media for scene/audio features (duration, loudness, speech-to-text)
- POST /api/v1/analysis/transcribe — generate transcript (third-party or local)
- POST /api/v1/analysis/labels — auto-label content (NLP/vision)
- GET  /api/v1/analysis/{id}/report — retrieve analysis report

## Metadata Management APIs (3)
- GET  /api/v1/tags — list all tags and counts
- POST /api/v1/tags/{id}/add — add tag(s) to content
- POST /api/v1/tags/{id}/remove — remove tag(s) from content

## Monitoring, Logging, Testing, Docs & Admin (6)
- GET  /api/v1/health — health check (ready/live)
- GET  /api/v1/metrics — Prometheus-style metrics endpoint
- GET  /api/v1/logs — fetch recent service logs (admin, paginated)
- GET  /api/v1/docs — OpenAPI/Swagger JSON
- GET  /api/v1/docs/ui — interactive docs (Swagger UI)
- POST /api/v1/tests/run — run API test suite (returns results)

## Auth & Optimization notes
- New API will support versioning via path (`/api/v1/...`) and forward-compatibility.
- Per request from task, initial design will remove rate-limiting and authentication by default; this can be toggled by runtime config or middleware.

## Default Presets Suggestion (summary)
- Audio presets: 48kbps, 64kbps (ADD), 96kbps, 128kbps, 192kbps, 256kbps, 320kbps
- Video presets: 144p, 240p, 360p, 480p, 720p, 1080p, 1440p, 2160p(4K)
- Subtitle defaults: enable English priority, subtitle modes `prefer_manual` by default
- Audio language priority: Bangla, Hindi, English

## Next steps
1. Review and approve endpoint groups and naming conventions.
2. Produce OpenAPI v3 spec for `/api/v1` with schemas and examples.
3. Implement route scaffolding in `app/api_v1.py` and wire into `app/main.py` (versioned).
4. Implement presets, metadata extraction, thumbnail embedding, and tests incrementally.

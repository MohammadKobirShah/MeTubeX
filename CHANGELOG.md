# Changelog

All notable changes to this project are documented in this file.

## Unreleased

- Add versioned API scaffold under `/api/v1/` with endpoints for downloads, presets, metadata, thumbnails, search, jobs, and analysis.
- Implement `app/presets.py` with default audio/video presets (added 64kbps audio preset).
- Add metadata extraction (`app/metadata.py`) and thumbnail helper (`app/thumbnails.py`).
- Add `JobManager` for batch job processing (`app/jobs.py`) with persistence and job results endpoint.
- Implement search index (`app/search_index.py`) with endpoints to index and search; auto-index job results.
- Add analysis placeholders (`app/analysis.py`) with transcribe/label endpoints.
- Add OpenAPI spec and serve it at `/api/v1/docs/openapi.yaml` and a Swagger UI at `/api/v1/docs/ui`.
- Add monitoring (`app/monitoring.py`) + `/api/v1/metrics` and job counters (Prometheus optional).
- Add middleware for optional API auth, rate limiting, and API version negotiation (`app/middleware.py`).
- Add structured JSON logging support (`app/logging_config.py`) and optional config flags.
- Add tests for search and job indexing (`app/tests/test_search_and_jobs.py`).

### Notes

- Many features are scaffolded (search ranking, metadata CRUD, job orchestration, analysis integrations). See `docs/API_EXPANSION_PLAN.md` for next steps.
- Thumbnail embedding requires `ffmpeg` available on PATH for embedding into media files.

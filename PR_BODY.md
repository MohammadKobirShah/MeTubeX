Title: Feature/API expansion — v1 (metadata, thumbnails, jobs, search, analysis)

Summary:
- Implements a versioned API at `/api/v1/` and scaffolds a broad set of media-related endpoints.

Key changes:
- `app/api_v1.py`: new versioned endpoints (downloads, presets, metadata, thumbnails, search, jobs, analysis, docs, metrics).
- `app/presets.py`: presets store + defaults.
- `app/metadata.py`, `app/thumbnails.py`: metadata extraction and thumbnail utilities.
- `app/jobs.py`: batch job manager with persistence and auto-indexing.
- `app/search_index.py`: simple persistent search index and endpoints.
- `app/analysis.py`: placeholder analysis functions + endpoints.
- `app/middleware.py`: auth, rate-limit, and versioning middleware.
- `app/monitoring.py`: Prometheus-compatible metrics helpers.
- `app/logging_config.py`: structured JSON logging support.
- `app/tests/test_search_and_jobs.py`: tests for search + job auto-indexing.

Why:
- Expand API surface to support metadata extraction, batch processing, and discovery features required by frontend and integrations.

Notes for reviewers:
- Many endpoints are initial scaffolds and will need production hardening (security, distributed rate-limiting, resilient job queue, full-text search engine).
- See `CHANGELOG.md` and `docs/API_EXPANSION_PLAN.md` for a detailed roadmap.

Suggested next steps after merge:
1. Implement persistent metadata CRUD and link to downloads.
2. Add robust job orchestration and status updates (job queue backed by Redis/RQ/Celery).
3. Integrate real transcription/labeling models or external services.
4. Add CI checks for linting and tests.

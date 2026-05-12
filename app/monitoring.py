"""Lightweight monitoring helpers with optional Prometheus support.

If `prometheus_client` is installed, metrics are exposed in Prometheus format.
Otherwise `get_metrics()` returns a simple plaintext summary.
"""
from typing import Optional
import time
import logging

log = logging.getLogger('monitoring')

try:
    from prometheus_client import CollectorRegistry, Counter, generate_latest, CONTENT_TYPE_LATEST
    PROM_AVAILABLE = True
except Exception:
    PROM_AVAILABLE = False

if PROM_AVAILABLE:
    registry = CollectorRegistry()
    downloads_submitted = Counter('metube_downloads_submitted_total', 'Total downloads submitted', registry=registry)
    jobs_created = Counter('metube_jobs_created_total', 'Total jobs created', registry=registry)
    jobs_completed = Counter('metube_jobs_completed_total', 'Total jobs completed', registry=registry)
    jobs_failed = Counter('metube_jobs_failed_total', 'Total jobs failed', registry=registry)


def incr_downloads_submitted(n: int = 1):
    if PROM_AVAILABLE:
        downloads_submitted.inc(n)


def incr_job_created(n: int = 1):
    if PROM_AVAILABLE:
        jobs_created.inc(n)


def incr_job_completed(n: int = 1):
    if PROM_AVAILABLE:
        jobs_completed.inc(n)


def incr_job_failed(n: int = 1):
    if PROM_AVAILABLE:
        jobs_failed.inc(n)


def get_metrics() -> tuple[bytes, str]:
    """Return tuple (body, content_type)."""
    if PROM_AVAILABLE:
        return generate_latest(registry), CONTENT_TYPE_LATEST
    # Fallback plain text
    body = []
    body.append(f"downloads_submitted: UNKNOWN (prometheus_client not installed)")
    return ("\n".join(body).encode('utf-8'), 'text/plain; charset=utf-8')

import time
import os
from aiohttp import web


def create_auth_middleware(config):
    @web.middleware
    async def auth_middleware(request, handler):
        # Only apply to API routes
        if not getattr(config, 'ENABLE_API_AUTH', False):
            return await handler(request)
        path = str(request.rel_url.path)
        if not path.startswith('/api/'):
            return await handler(request)
        key = request.headers.get('X-API-KEY') or request.rel_url.query.get('api_key')
        if not key or key != getattr(config, 'API_KEY', ''):
            return web.Response(status=401, text='{"error":"unauthorized"}', content_type='application/json')
        return await handler(request)

    return auth_middleware


def create_rate_limit_middleware(config):
    # Simple in-memory fixed-window rate limiter per remote address
    store = {}
    window = 60
    try:
        limit = int(getattr(config, 'RATE_LIMIT_PER_MINUTE', 60))
    except Exception:
        limit = 60

    @web.middleware
    async def rate_middleware(request, handler):
        if not getattr(config, 'ENABLE_RATE_LIMIT', False):
            return await handler(request)
        path = str(request.rel_url.path)
        if not path.startswith('/api/'):
            return await handler(request)
        peer = request.remote or 'unknown'
        now = int(time.time())
        rec = store.get(peer)
        if not rec or now - rec['start'] >= window:
            store[peer] = {'count': 1, 'start': now}
        else:
            if rec['count'] >= limit:
                return web.Response(status=429, text='{"error":"rate_limited"}', content_type='application/json')
            rec['count'] += 1
        return await handler(request)

    return rate_middleware


def create_version_middleware(config):
    supported = [s.strip() for s in str(getattr(config, 'SUPPORTED_API_VERSIONS', '')).split(',') if s.strip()]
    if not supported:
        supported = ['v1']

    @web.middleware
    async def version_middleware(request, handler):
        path = str(request.rel_url.path)
        if not path.startswith('/api/'):
            resp = await handler(request)
            resp.headers['X-API-Version'] = supported[0]
            return resp

        # Check headers, prefer explicit header
        requested = request.headers.get('X-API-Version') or request.headers.get('Accept-Version')
        if requested:
            if requested not in supported:
                return web.Response(status=426, text='{"error":"unsupported_api_version"}', content_type='application/json')
            version = requested
        else:
            # infer from path (/api/v1/...)
            parts = path.split('/')
            if len(parts) > 2 and parts[2]:
                candidate = parts[2]
                if candidate in supported:
                    version = candidate
                else:
                    version = supported[0]
            else:
                version = supported[0]

        resp = await handler(request)
        resp.headers['X-API-Version'] = version
        return resp

    return version_middleware

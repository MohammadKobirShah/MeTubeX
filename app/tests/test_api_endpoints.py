import pytest
from aiohttp import web

from app import main as main_mod


@pytest.fixture
def client(loop, aiohttp_client):
    return loop.run_until_complete(aiohttp_client(main_mod.app))


@pytest.mark.asyncio
async def test_version_endpoint(client):
    resp = await client.get('/api/v1/version')
    assert resp.status == 200
    data = await resp.json()
    assert 'version' in data


@pytest.mark.asyncio
async def test_docs_and_ui(client):
    r = await client.get('/api/v1/docs/openapi.yaml')
    assert r.status == 200
    text = await r.text()
    assert 'openapi' in text

    r2 = await client.get('/api/v1/docs/ui')
    assert r2.status == 200
    html = await r2.text()
    assert '<title>Metube API Docs' in html or 'SwaggerUIBundle' in html


@pytest.mark.asyncio
async def test_search_metrics(client):
    r = await client.get('/api/v1/search?q=test')
    assert r.status == 200
    data = await r.json()
    assert 'total' in data and 'items' in data

    r2 = await client.get('/api/v1/metrics')
    # metrics may be text/plain or prometheus format; just ensure 200
    assert r2.status == 200

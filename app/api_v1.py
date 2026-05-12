from aiohttp import web
import json
import os
from app.presets import PresetStore
from app import metadata as metadata_mod
from app import thumbnails as thumbnails_mod
import yt_dlp as _yt_dlp
from app.jobs import JobManager
from app.search_index import SearchIndex
from app import analysis as analysis_mod
from app import monitoring as monitoring_mod


def register_routes(app, config, dqueue, submgr, serializer, sio, parse_download_options):
    routes = web.RouteTableDef()
    # Presets persisted in STATE_DIR/presets.json
    preset_store = PresetStore(config.STATE_DIR)
    # Search index
    search_index = SearchIndex(config.STATE_DIR)
    # Job manager for background batch processing (auto-index results via search_index.add)
    job_manager = JobManager(config.STATE_DIR, dqueue, result_hook=search_index.add)

    @routes.get('/api/v1/version')
    async def version(request):
        return web.json_response({
            "yt-dlp": os.getenv("YT_DLP_VERSION", "unknown"),
            "version": os.getenv("METUBE_VERSION", "dev"),
        })

    @routes.get('/api/v1/docs/openapi.yaml')
    async def openapi_yaml(request):
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'docs', 'openapi_v1.yaml')
        if not os.path.exists(path):
            raise web.HTTPNotFound()
        with open(path, encoding='utf-8') as f:
            content = f.read()
        return web.Response(text=content, content_type='application/x-yaml')

    @routes.get('/api/v1/docs/ui')
    async def docs_ui(request):
        html = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>MeTube API Docs</title>
    <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css">
    <style>
        body { margin: 0; padding: 0; }
    </style>
</head>
<body>
    <div id="swagger-ui"></div>
    <script src="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
    <script>
        window.ui = SwaggerUIBundle({
            url: '/api/v1/docs/openapi.yaml',
            dom_id: '#swagger-ui',
            deepLinking: true,
            showExtensions: true,
            showCommonExtensions: true,
        });
    </script>
</body>
</html>'''
        return web.Response(text=html, content_type='text/html')

    @routes.post('/api/v1/downloads/add')
    async def add(request):
        try:
            post = await request.json()
        except json.JSONDecodeError:
            raise web.HTTPBadRequest(reason='Invalid JSON')
        try:
            o = parse_download_options(post)
        except web.HTTPBadRequest:
            raise
        status = await dqueue.add(
            o['url'],
            o['download_type'],
            o['codec'],
            o['format'],
            o['quality'],
            o['folder'],
            o['custom_name_prefix'],
            o['playlist_item_limit'],
            o['auto_start'],
            o['split_by_chapters'],
            o['chapter_template'],
            o['subtitle_language'],
            o['subtitle_mode'],
            o['ytdl_options_presets'],
            o['ytdl_options_overrides'],
            o['clip_start'],
            o['clip_end'],
        )
        return web.Response(text=serializer.encode(status), content_type='application/json')

    @routes.post('/api/v1/downloads/add-batch')
    async def add_batch(request):
        post = await request.json()
        items = post.get('items') or []
        results = []
        for item in items:
            try:
                o = parse_download_options(item)
            except web.HTTPBadRequest as e:
                results.append({'status': 'error', 'msg': str(e.reason)})
                continue
            res = await dqueue.add(
                o['url'],
                o['download_type'],
                o['codec'],
                o['format'],
                o['quality'],
                o['folder'],
                o['custom_name_prefix'],
                o['playlist_item_limit'],
                o['auto_start'],
                o['split_by_chapters'],
                o['chapter_template'],
                o['subtitle_language'],
                o['subtitle_mode'],
                o['ytdl_options_presets'],
                o['ytdl_options_overrides'],
                o['clip_start'],
                o['clip_end'],
            )
            results.append(res)
        return web.Response(text=serializer.encode({'results': results}), content_type='application/json')

    @routes.get('/api/v1/downloads')
    async def downloads_list(request):
        try:
            data = dqueue.get()
            return web.Response(text=serializer.encode(data), content_type='application/json')
        except Exception as e:
            raise web.HTTPInternalServerError(reason=str(e))

    @routes.get('/api/v1/downloads/{id}')
    async def download_get(request):
        id = request.match_info.get('id')
        # Look in queue, pending, then done
        for collection in (dqueue.queue, dqueue.pending, dqueue.done):
            if collection.exists(id):
                dl = collection.get(id)
                return web.Response(text=serializer.encode(dl.info), content_type='application/json')
        raise web.HTTPNotFound()

    @routes.post('/api/v1/thumbnails/generate')
    async def thumbnails_generate(request):
        post = await request.json()
        url = post.get('url')
        if not url:
            raise web.HTTPBadRequest(reason='missing url')
        try:
            opts = dict(getattr(config, 'YTDL_OPTIONS', {}))
            params = {**opts, 'skip_download': True, 'writethumbnail': True}
            with _yt_dlp.YoutubeDL(params=params) as ydl:
                ydl.download([url])
            return web.Response(text=serializer.encode({'status': 'ok', 'msg': 'thumbnail generation attempted (check temp files)'}), content_type='application/json')
        except Exception as e:
            raise web.HTTPInternalServerError(reason=str(e))

    @routes.get('/api/v1/metadata/extract')
    async def metadata_extract(request):
        url = request.rel_url.query.get('url')
        if not url:
            raise web.HTTPBadRequest(reason='missing url')
        try:
            md = metadata_mod.extract_from_url(url, getattr(config, 'YTDL_OPTIONS', {}))
            return web.Response(text=serializer.encode(md), content_type='application/json')
        except Exception as e:
            raise web.HTTPInternalServerError(reason=str(e))

    @routes.post('/api/v1/metadata/extract-batch')
    async def metadata_extract_batch(request):
        post = await request.json()
        items = post.get('items') or []
        try:
            res = metadata_mod.extract_batch(items, getattr(config, 'YTDL_OPTIONS', {}))
            return web.Response(text=serializer.encode({'results': res}), content_type='application/json')
        except Exception as e:
            raise web.HTTPInternalServerError(reason=str(e))

    @routes.post('/api/v1/thumbnails/embed')
    async def thumbnails_embed(request):
        post = await request.json()
        media = post.get('media_path')
        thumb = post.get('thumbnail_path') or post.get('thumbnail_url')
        if not media or not thumb:
            raise web.HTTPBadRequest(reason='media_path and thumbnail_path/thumbnail_url required')
        if not os.path.isabs(media):
            media = os.path.join(config.DOWNLOAD_DIR, media)
        try:
            out = thumbnails_mod.embed_thumbnail(media, thumb)
            return web.Response(text=serializer.encode({'status': 'ok', 'path': out}), content_type='application/json')
        except Exception as e:
            raise web.HTTPInternalServerError(reason=str(e))

    @routes.post('/api/v1/jobs/batch-add')
    async def jobs_batch_add(request):
        post = await request.json()
        items = post.get('items') or []
        if not isinstance(items, list) or not items:
            raise web.HTTPBadRequest(reason='items must be a non-empty array')
        name = post.get('name')
        job_id = job_manager.create_batch_job(items, name=name)
        try:
            monitoring_mod.incr_job_created()
        except Exception:
            pass
        return web.Response(text=serializer.encode({'job_id': job_id, 'status': 'accepted'}), content_type='application/json')

    @routes.get('/api/v1/jobs/{job_id}')
    async def jobs_get(request):
        job_id = request.match_info.get('job_id')
        job = job_manager.get(job_id)
        if not job:
            raise web.HTTPNotFound()
        return web.Response(text=serializer.encode(job), content_type='application/json')

    @routes.get('/api/v1/jobs')
    async def jobs_list(request):
        return web.Response(text=serializer.encode(job_manager.list_jobs()), content_type='application/json')

    @routes.post('/api/v1/jobs/cancel')
    async def jobs_cancel(request):
        post = await request.json()
        job_id = post.get('job_id')
        if not job_id:
            raise web.HTTPBadRequest(reason='job_id required')
        ok = job_manager.cancel_job(job_id)
        if not ok:
            raise web.HTTPNotFound()
        return web.Response(text=serializer.encode({'status': 'canceled', 'job_id': job_id}), content_type='application/json')

    @routes.get('/api/v1/jobs/{job_id}/results')
    async def jobs_results(request):
        job_id = request.match_info.get('job_id')
        job = job_manager.get(job_id)
        if not job:
            raise web.HTTPNotFound()
        try:
            page = int(request.rel_url.query.get('page', '1'))
            per_page = int(request.rel_url.query.get('per_page', '20'))
        except ValueError:
            raise web.HTTPBadRequest(reason='page and per_page must be integers')
        results = job.get('results') or []
        total = len(results)
        start = max(0, (page - 1) * per_page)
        end = start + per_page
        page_items = results[start:end]
        return web.Response(text=serializer.encode({'total': total, 'page': page, 'per_page': per_page, 'items': page_items}), content_type='application/json')

    @routes.get('/api/v1/search')
    async def search(request):
        q = request.rel_url.query.get('q', '')
        if not q:
            return web.Response(text=serializer.encode({'total': 0, 'items': []}), content_type='application/json')
        try:
            page = int(request.rel_url.query.get('page', '1'))
            per_page = int(request.rel_url.query.get('per_page', '20'))
        except ValueError:
            raise web.HTTPBadRequest(reason='page and per_page must be integers')
        results = search_index.search(q, limit=1000)
        total = len(results)
        start = max(0, (page - 1) * per_page)
        end = start + per_page
        items = results[start:end]
        return web.Response(text=serializer.encode({'total': total, 'page': page, 'per_page': per_page, 'items': items}), content_type='application/json')

    @routes.post('/api/v1/search/index')
    async def search_index_post(request):
        post = await request.json()
        try:
            search_index.add(post)
            return web.Response(text=serializer.encode({'status': 'ok', 'id': post.get('id')}), content_type='application/json')
        except Exception as e:
            raise web.HTTPBadRequest(reason=str(e))

    @routes.post('/api/v1/search/reindex')
    async def search_reindex(request):
        # Reindex metadata found in job results
        count = search_index.reindex_from_jobs(job_manager)
        return web.Response(text=serializer.encode({'reindexed': count}), content_type='application/json')

    @routes.get('/api/v1/metrics')
    async def metrics(request):
        body, ctype = monitoring_mod.get_metrics()
        return web.Response(body=body, content_type=ctype)

    @routes.post('/api/v1/analysis/transcribe')
    async def analysis_transcribe(request):
        post = await request.json()
        media = post.get('media_path')
        if not media:
            raise web.HTTPBadRequest(reason='media_path required')
        if not os.path.isabs(media):
            media = os.path.join(config.DOWNLOAD_DIR, media)
        try:
            # run blocking work in thread
            result = await request.app.loop.run_in_executor(None, analysis_mod.transcribe_media, media)
            return web.Response(text=serializer.encode(result), content_type='application/json')
        except FileNotFoundError:
            raise web.HTTPNotFound()
        except Exception as e:
            raise web.HTTPInternalServerError(reason=str(e))

    @routes.post('/api/v1/analysis/label')
    async def analysis_label(request):
        post = await request.json()
        media = post.get('media_path')
        if not media:
            raise web.HTTPBadRequest(reason='media_path required')
        if not os.path.isabs(media):
            media = os.path.join(config.DOWNLOAD_DIR, media)
        try:
            result = await request.app.loop.run_in_executor(None, analysis_mod.label_media, media)
            return web.Response(text=serializer.encode(result), content_type='application/json')
        except FileNotFoundError:
            raise web.HTTPNotFound()
        except Exception as e:
            raise web.HTTPInternalServerError(reason=str(e))

    @routes.get('/api/v1/presets/audio')
    async def presets_audio_get(request):
        return web.Response(text=serializer.encode(preset_store.list_audio()), content_type='application/json')

    @routes.post('/api/v1/presets/audio')
    async def presets_audio_post(request):
        post = await request.json()
        name = post.get('name')
        spec = {k: v for k, v in post.items() if k != 'name'}
        if not name:
            raise web.HTTPBadRequest(reason='preset name required')
        preset_store.set_audio(name, spec)
        return web.Response(text=serializer.encode({'status': 'ok', 'name': name}), content_type='application/json')

    @routes.get('/api/v1/presets/video')
    async def presets_video_get(request):
        return web.Response(text=serializer.encode(preset_store.list_video()), content_type='application/json')

    @routes.post('/api/v1/presets/video')
    async def presets_video_post(request):
        post = await request.json()
        name = post.get('name')
        spec = {k: v for k, v in post.items() if k != 'name'}
        if not name:
            raise web.HTTPBadRequest(reason='preset name required')
        preset_store.set_video(name, spec)
        return web.Response(text=serializer.encode({'status': 'ok', 'name': name}), content_type='application/json')

    app.add_routes(routes)

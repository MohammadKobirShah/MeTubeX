import logging


def configure_json_logging(config):
    """Configure root logger to emit JSON logs when `ENABLE_JSON_LOGGING` is true.

    Falls back to standard logging if `python-json-logger` is not installed.
    """
    enabled = getattr(config, 'ENABLE_JSON_LOGGING', False)
    if not enabled:
        return
    try:
        from pythonjsonlogger import jsonlogger
    except Exception:
        # library not available; skip
        return

    root = logging.getLogger()
    # Remove existing handlers and use a single stream handler with JSON formatter
    for h in list(root.handlers):
        root.removeHandler(h)
    handler = logging.StreamHandler()
    fmt = jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(name)s %(message)s')
    handler.setFormatter(fmt)
    root.addHandler(handler)
    level = getattr(logging, str(getattr(config, 'LOGLEVEL', 'INFO')).upper(), logging.INFO)
    root.setLevel(level)

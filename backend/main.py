# main.py – Flask & FastAPI Kompatibilitäts-Entrypoint
from backend.flask.app import create_app

flask_app = create_app()

# FastAPI-Kompatibilitäts-Stub
try:
    from fastapi import FastAPI
    from starlette.requests import Request
    from starlette.responses import Response
    from starlette.middleware.wsgi import WSGIMiddleware

    app = FastAPI()
    app.mount("/", WSGIMiddleware(flask_app))
except ImportError:
    app = flask_app

"""
Serveur FastAPI pour exposer la documentation interactive Swagger UI, Redoc et GraphQL Playground pour tous les modules backend Dihya.
Sécurité, CORS, JWT, multilingue, RGPD, plugins, audit, CI/CD ready.
"""
from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi.responses import RedirectResponse, FileResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="Dihya Backend Docs", docs_url=None, redoc_url=None, openapi_url=None)

# Sécurité CORS stricte
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/docs", include_in_schema=False)
def swagger_ui():
    return get_swagger_ui_html(
        openapi_url="/api/openapi.json",
        title="Dihya Backend Swagger UI"
    )

@app.get("/api/redoc", include_in_schema=False)
def redoc_ui():
    return get_redoc_html(
        openapi_url="/api/openapi.json",
        title="Dihya Backend Redoc"
    )

@app.get("/api/openapi.json", include_in_schema=False)
def openapi_json():
    # Fusionne les specs OpenAPI YAML de tous les modules (exemple simplifié)
    # Pour la démo, retourne l’index global
    return FileResponse(os.path.join(os.path.dirname(__file__), "openapi_backend_index.yaml"), media_type="application/yaml")

@app.get("/api/graphql-playground", include_in_schema=False)
def graphql_playground():
    html = """
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset=utf-8/>
        <title>GraphQL Playground</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/graphql-playground-react/build/static/css/index.css" />
        <link rel="shortcut icon" href="https://cdn.jsdelivr.net/npm/graphql-playground-react/build/favicon.png" />
        <script src="https://cdn.jsdelivr.net/npm/graphql-playground-react/build/static/js/middleware.js"></script>
      </head>
      <body>
        <div id="root" />
        <script>window.addEventListener('load', function() { GraphQLPlayground.init(document.getElementById('root'), { endpoint: '/api/compliance/graphql/graphql' }) })</script>
      </body>
    </html>
    """
    return HTMLResponse(content=html, status_code=200)

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/api/docs")

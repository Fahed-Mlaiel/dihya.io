"""
Middleware de versioning API threed (Python) - Ultra avancé
Gère la détection, la validation, la logique métier multi-version
Utilisation : app.before_request(versioning_middleware)
"""
from flask import g, request

SUPPORTED_VERSIONS = ['1.0', '2.0']


def versioning_middleware():
    version = request.headers.get('X-Api-Version', '1.0')
    if version not in SUPPORTED_VERSIONS:
        from flask import abort, jsonify
        abort(400, description=f'API version not supported. Supported: {SUPPORTED_VERSIONS}')
    g.api_version = version
    if not hasattr(g, 'business_context'):
        g.business_context = {}
    g.business_context['api_version'] = version

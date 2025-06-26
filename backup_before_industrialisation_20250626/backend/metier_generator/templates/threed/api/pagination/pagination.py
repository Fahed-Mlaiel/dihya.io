"""
Middleware de pagination API threed (Python) - Ultra avancé
Gère la validation, les bornes, la doc, l'intégration métier
Utilisation : app.before_request(pagination_middleware)
"""
from flask import g, request


def pagination_middleware():
    try:
        page = int(request.args.get('page', 1))
        size = int(request.args.get('size', 10))
    except Exception:
        page, size = 1, 10
    if page < 1:
        page = 1
    if size < 1 or size > 100:
        size = 10
    g.pagination = {'page': page, 'size': size}
    if not hasattr(g, 'business_context'):
        g.business_context = {}
    g.business_context['pagination'] = g.pagination

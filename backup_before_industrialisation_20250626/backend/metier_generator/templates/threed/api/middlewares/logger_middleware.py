"""
Middleware logger API threed (Python) - Ultra avancé
Journalisation structurée, corrélation, log métier, exportable
Utilisation : app.before_request(logger_middleware)
"""
import uuid
import time
from flask import g, request


def logger_middleware():
    if not hasattr(g, 'correlation_id'):
        g.correlation_id = request.headers.get('X-Correlation-Id', str(uuid.uuid4()))
    g.start_time = time.time()

    @request.after_this_request
    def log_response(response):
        duration = int((time.time() - g.start_time) * 1000)
        log = {
            'correlationId': g.correlation_id,
            'method': request.method,
            'url': request.path,
            'status': response.status_code,
            'duration': duration,
            'user': getattr(g, 'user_id', None),
            'businessContext': getattr(g, 'business_context', None)
        }
        print('[API-LOG]', log)
        return response

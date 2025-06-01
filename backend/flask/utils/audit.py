"""
Audit logging structuré, RGPD, accessibilité, plugins
"""
import structlog
logger = structlog.get_logger('audit')

def log_audit(request, response):
    logger.info('audit',
        path=request.path,
        method=request.method,
        status=response.status_code,
        user=request.headers.get('Authorization', 'anonymous'),
        ip=request.remote_addr)

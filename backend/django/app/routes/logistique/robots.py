"""
robots.py – Directives SEO dynamiques pour le module logistique (Dihya Coding)
Conformité RGPD, logs d’accès, multilingue, auditabilité.
"""
from django.http import HttpResponse
from .logs import log_access

def robots_txt(request):
    log_access(request, action="robots.txt_access")
    content = "User-agent: *\nDisallow: /private/\nAllow: /"
    return HttpResponse(content, content_type="text/plain")

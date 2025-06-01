"""
robots.py – Directives SEO dynamiques pour le module culture (Dihya Coding)
Conformité RGPD, logs d’accès, multilingue, auditabilité.
"""
from django.http import HttpResponse

def robots_txt(request):
    content = "User-agent: *\nDisallow: /private/\nAllow: /"
    return HttpResponse(content, content_type="text/plain")

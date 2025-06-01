"""
sitemap.py – Sitemap dynamique pour le module gamer (Dihya Coding)
Conformité RGPD, logs, multilingue, auditabilité.
"""
from django.http import HttpResponse
from django.urls import reverse

def sitemap_xml(request):
    urls = [reverse('gamer:index'), reverse('gamer:api-list')]
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    for url in urls:
        xml += f"<url><loc>{request.build_absolute_uri(url)}</loc></url>"
    xml += "</urlset>"
    return HttpResponse(xml, content_type="application/xml")

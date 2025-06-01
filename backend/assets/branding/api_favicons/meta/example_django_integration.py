# Dihya API Favicon – Exemple d’intégration REST/GraphQL Django

from django.http import JsonResponse
from Dihya.backend.assets.branding.api_favicons.meta.meta_favicon_api import meta_favicon_api

def favicon_meta_view(request):
    """
    Endpoint sécurisé, multilingue, RGPD, audit, accessibilité, SEO-ready.
    GET /api/meta/favicon
    """
    return JsonResponse(meta_favicon_api)

# Pour GraphQL, exposez meta_favicon_api comme un resolver ou un champ Query.

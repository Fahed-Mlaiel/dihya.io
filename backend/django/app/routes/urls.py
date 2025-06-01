"""
Routes globales Dihya (REST/GraphQL, sécurité maximale, multilingue, RGPD, plugins, audit, multitenant, fallback IA open source)
"""
from django.urls import path, include

urlpatterns = [
    path('compliance/', include('Dihya.backend.django.app.routes.compliance.urls')),
    path('intelligence-artificielle/', include('Dihya.backend.django.app.routes.intelligence_artificielle.routes')),
    path('vr-ar/', include('Dihya.backend.django.app.routes.vr_ar.urls')),
    # ...ajouter ici les autres modules métiers (logistique, santé, etc.)
]

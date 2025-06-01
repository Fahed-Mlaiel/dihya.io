"""
Routes backend Django pour la gestion 3D (Dihya)
Ultra avancé, sécurisé, multilingue, REST & GraphQL-ready, RGPD, plugins, audit, multitenancy.

Internationalisation dynamique (fr, en, ar, tzm, de, zh, ja, ko, nl, he, fa, hi, es).
Sécurité maximale (CORS, JWT, validation, audit, WAF, anti-DDOS, RBAC, RGPD, plugins, multitenancy).
Documentation intégrée, extensibilité, SEO backend (robots, sitemap dynamique, logs structurés).
Exemple d’extension plugin et fallback IA open source (LLaMA, Mixtral, Mistral).
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ThreeDProjectViewSet, ThreeDAssetViewSet
from .schemas import ThreeDProjectSchema, ThreeDAssetSchema
from .plugins import *
from .audit import *
from .i18n import *
from .permissions import *

# RESTful API
router = DefaultRouter()
router.register(r'threedprojects', ThreeDProjectViewSet, basename='3d-threedproject')
router.register(r'threedassets', ThreeDAssetViewSet, basename='3d-threedasset')

urlpatterns = [
    path('', include(router.urls)),
    # GraphQL endpoint (à brancher sur la stack GraphQL du projet)
    # path('graphql/', GraphQLView.as_view(graphiql=True)),
]

# Sécurité avancée, CORS, JWT, audit, WAF, anti-DDOS, RBAC, i18n, RGPD, plugins, multitenancy sont gérés dans les middlewares globaux du projet et dans chaque ViewSet.

# Exemple d’extension plugin 3D (ajout via API ou CLI)
# from .plugins import register_plugin
# register_plugin('llama_fallback', LLaMAFallbackPlugin)
# register_plugin('mixtral', MixtralPlugin)
# register_plugin('mistral', MistralPlugin)

# SEO backend : robots.txt, sitemap.xml, logs structurés générés dynamiquement dans le module SEO global.

# RGPD : endpoints d’export/anonymisation disponibles via les permissions et les plugins RGPD.

# Pour toute extension, voir la documentation plugins et la docstring de chaque ViewSet.

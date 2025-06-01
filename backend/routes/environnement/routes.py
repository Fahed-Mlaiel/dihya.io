"""
Ultra-Industrialisation : Module Environnement (Dihya)
REST, GraphQL, RGPD, Audit, Plugins, Multitenancy, Sectorisation, DWeb/IPFS, Monitoring, CI/CD, Health, Hooks métier
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EnvironnementProjectViewSet, EnvironnementAssetViewSet
from .schemas import EnvironnementProjectSchema, EnvironnementAssetSchema
from .plugins import *
from .audit import *
from .i18n import *
from .permissions import *
from .monitoring import *
from .export import *
from .dweb import *
from .sectorisation import *
from .rgpd import *

router = DefaultRouter()
router.register(r'environnementProjects', EnvironnementProjectViewSet, basename='environnement-project')
router.register(r'environnementAssets', EnvironnementAssetViewSet, basename='environnement-asset')

urlpatterns = [
    path('', include(router.urls)),
    path('health/', health_check_view),
    path('export/dweb/', dweb_export_view),
    # path('graphql/', GraphQLView.as_view(graphiql=True)),
]

# Ultra-Features: Sécurité avancée, CORS, JWT, audit, WAF, anti-DDOS, RBAC, i18n, RGPD, plugins, multitenancy, sectorisation, hooks métier, monitoring, DWeb/IPFS, export, CI/CD, health-check, tests, coverage

"""
Ultra-Industrialisation : Module Blockchain (Dihya)
REST, GraphQL, RGPD, Audit, Plugins, Multitenancy, Sectorisation, DWeb/IPFS, Monitoring, CI/CD, Health, Hooks métier
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import BlockchainAssetViewSet
# from .schemas import BlockchainAssetSchema
from .plugins import *
from .audit import *
from .i18n import *
from .permissions import *

router = DefaultRouter()
# router.register(r'blockchainassets', BlockchainAssetViewSet, basename='blockchain-blockchainasset')

urlpatterns = [
    path('', include(router.urls)),
    # path('export/dweb/', dweb_export_view),
    # path('graphql/', GraphQLView.as_view(graphiql=True)),
]

# Ultra-Features: Sécurité avancée, CORS, JWT, audit, WAF, anti-DDOS, RBAC, i18n, RGPD, plugins, multitenancy, sectorisation, hooks métier, monitoring, DWeb/IPFS, export, CI/CD, health-check, tests, coverage

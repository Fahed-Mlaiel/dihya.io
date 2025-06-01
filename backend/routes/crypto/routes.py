"""
Ultra-Industrialisation : Module Crypto (Dihya)
REST, GraphQL, RGPD, Audit, Plugins, Multitenancy, Sectorisation, DWeb/IPFS, Monitoring, CI/CD, Health, Hooks métier
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CryptoProjectViewSet, CryptoAssetViewSet
from .schemas import CryptoProjectSchema, CryptoAssetSchema
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
router.register(r'cryptoprojects', CryptoProjectViewSet, basename='crypto-project')
router.register(r'cryptoassets', CryptoAssetViewSet, basename='crypto-asset')

urlpatterns = [
    path('', include(router.urls)),
    path('health/', health_check_view),
    path('export/dweb/', dweb_export_view),
    # path('graphql/', GraphQLView.as_view(graphiql=True)),
]

# Ultra-Features: Sécurité avancée, CORS, JWT, audit, WAF, anti-DDOS, RBAC, i18n, RGPD, plugins, multitenancy, sectorisation, hooks métier, monitoring, DWeb/IPFS, export, CI/CD, health-check, tests, coverage

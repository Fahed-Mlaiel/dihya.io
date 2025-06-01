"""
Fichier d'initialisation du module Django routes/blockchain
Expose toutes les fonctionnalités REST, GraphQL, plugins, sécurité, i18n, audit, RGPD, multitenancy, etc.
Ultra avancé, production-ready, multilingue, souverain, extensible, sécurisé.
"""
from .routes import urlpatterns
from .schemas import BlockchainProjectSchema, BlockchainAssetSchema, BlockchainProjectListSchema, BlockchainAssetListSchema
from .plugins import *
from .audit import *
from .i18n import *
from .permissions import *
from .models import *
from .serializers import *
from .templates import *

__all__ = [
    'urlpatterns',
    'BlockchainProjectSchema', 'BlockchainAssetSchema', 'BlockchainProjectListSchema', 'BlockchainAssetListSchema',
    'plugins', 'audit', 'i18n', 'permissions', 'models', 'serializers', 'templates'
]

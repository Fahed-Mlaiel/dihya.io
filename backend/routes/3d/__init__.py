"""
Initialisation du module Django routes/3d
Expose toutes les fonctionnalités REST, GraphQL, plugins, sécurité, i18n, audit, RGPD, multitenancy, SEO, logging, tests, monitoring.
Ultra avancé, production-ready, multilingue, souverain, extensible, sécurisé, CI-ready.
"""
from .routes import *
from .views import *
from .models import *
from .schemas import *
from .serializers import *
from .plugins import *
from .audit import *
from .i18n import *
from .permissions import *
from .policy import *
from .tests import *

__all__ = [
    'ThreeDProjectViewSet', 'ThreeDAssetViewSet', 'urlpatterns',
    'ThreeDProjectSchema', 'ThreeDAssetSchema', 'ThreeDProjectListSchema', 'ThreeDAssetListSchema',
    'plugins', 'audit', 'i18n', 'permissions', 'models', 'serializers', 'templates', 'policy', 'tests'
]

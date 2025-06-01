"""
Initialisation du module Django routes/vr_ar
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

__all__ = [
    'SceneViewSet', 'AssetViewSet', 'urlpatterns',
    'SceneSchema', 'AssetSchema', 'SceneListSchema', 'AssetListSchema',
    'plugins', 'audit', 'i18n', 'permissions', 'models', 'serializers', 'templates', 'policy'
]

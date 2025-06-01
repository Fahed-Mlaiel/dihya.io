"""
Entrypoint métier principal du module 3D (Dihya)
Contient la logique métier, les imports, et l’intégration des routes, modèles, plugins, etc.
"""
from .routes import *
from .models import *
from .plugins import *
from .schemas import *
from .serializers import *
from .views import *
from .audit import *
from .i18n import *
from .permissions import *
from .validators import *

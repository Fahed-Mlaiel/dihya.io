"""
Dihya Backend – Initialisation du module routes.vr_ar
Chargement dynamique des plugins, configuration i18n, sécurité, audit, RGPD, accessibilité, documentation avancée.
- Import automatique des endpoints, schémas, routes, plugins dynamiques, multilingue, production-ready.
- Extensible, souverain, CI/CD, accessibilité, RGPD, SEO backend.
"""
from .views import *
from .schemas import *
from .urls import urlpatterns
from .plugins import *

__all__ = ["urlpatterns"]

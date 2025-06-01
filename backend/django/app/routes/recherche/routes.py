"""
Dihya – Django Recherche API Routes Ultra Avancé
------------------------------------------------
- Endpoints REST pour recherche plein texte, suggestions, autocomplétion, facettes, IA recherche, logs, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, anonymisation, multilingue, extensibilité, fallback IA open source
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST recherche (sécurité, multilingue, souveraineté)
🇬🇧 Django REST search routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للبحث (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n unadi (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'', views.RechercheViewSet, basename='recherche')
router.register(r'suggestions', views.SuggestionViewSet, basename='suggestion')
router.register(r'autocomplete', views.AutocompleteViewSet, basename='autocomplete')
router.register(r'facettes', views.FacetteViewSet, basename='facette')
router.register(r'ia', views.IARechercheViewSet, basename='ia-recherche')
router.register(r'logs', views.LogRechercheViewSet, basename='log-recherche')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, anonymisation, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Fallback IA open source : tous les endpoints critiques disposent d’un fallback open source
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

"""
Dihya – Django Construction API Routes Ultra Avancé
--------------------------------------------------
- Endpoints REST pour projets, chantiers, ressources, matériaux, équipements, sous-traitants, incidents, BIM, logs, audit
- Sécurité, RBAC, logs, conformité RGPD/NIS2, multilingue, extensibilité
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST construction (sécurité, multilingue, souveraineté)
🇬🇧 Django REST construction routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للبناء (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n tnekra (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'projets', views.ProjetViewSet, basename='projet')
router.register(r'chantiers', views.ChantierViewSet, basename='chantier')
router.register(r'ressources', views.RessourceViewSet, basename='ressource')
router.register(r'materiaux', views.MateriauViewSet, basename='materiau')
router.register(r'equipements', views.EquipementViewSet, basename='equipement')
router.register(r'sous_traitants', views.SousTraitantViewSet, basename='sous-traitant')
router.register(r'incidents', views.IncidentViewSet, basename='incident')
router.register(r'bim', views.BIMViewSet, basename='bim')
router.register(r'rapports', views.RapportViewSet, basename='rapport')
router.register(r'alertes', views.AlerteViewSet, basename='alerte')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Extensible : ajoutez vos endpoints (BIM, IoT, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

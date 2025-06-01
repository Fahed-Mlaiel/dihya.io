"""
Dihya – Django Industrie API Routes Ultra Avancé
------------------------------------------------
- Endpoints REST pour usines, lignes de production, équipements, capteurs, incidents, maintenance, ordres de fabrication, stocks, IA industrielle, logs, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, multilingue, extensibilité
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST industrie (sécurité, multilingue, souveraineté)
🇬🇧 Django REST industry routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للصناعة (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n tnefsit (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'usines', views.UsineViewSet, basename='usine')
router.register(r'lignes', views.LigneProductionViewSet, basename='ligne-production')
router.register(r'equipements', views.EquipementViewSet, basename='equipement')
router.register(r'capteurs', views.CapteurViewSet, basename='capteur')
router.register(r'incidents', views.IncidentViewSet, basename='incident')
router.register(r'maintenances', views.MaintenanceViewSet, basename='maintenance')
router.register(r'ordres', views.OrdreFabricationViewSet, basename='ordre-fabrication')
router.register(r'stocks', views.StockViewSet, basename='stock')
router.register(r'ia', views.IAIndustrieViewSet, basename='ia-industrie')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

"""
Dihya – Django Énergie API Routes Ultra Avancé
----------------------------------------------
- Endpoints REST pour sites, compteurs, consommations, productions, alertes, factures, IoT, IA prédictive, logs, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, multilingue, extensibilité
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST énergie (sécurité, multilingue, souveraineté)
🇬🇧 Django REST energy routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للطاقة (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n tazult (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'sites', views.SiteViewSet, basename='site')
router.register(r'compteurs', views.CompteurViewSet, basename='compteur')
router.register(r'consommations', views.ConsommationViewSet, basename='consommation')
router.register(r'productions', views.ProductionViewSet, basename='production')
router.register(r'alertes', views.AlerteViewSet, basename='alerte')
router.register(r'factures', views.FactureViewSet, basename='facture')
router.register(r'iot', views.IoTViewSet, basename='iot')
router.register(r'ia', views.IAPredictionViewSet, basename='ia-prediction')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Extensible : ajoutez vos endpoints (analyse IA, IoT, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

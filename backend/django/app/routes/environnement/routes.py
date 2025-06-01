"""
Dihya – Django Environnement API Routes Ultra Avancé
---------------------------------------------------
- Endpoints REST pour sites, capteurs, mesures, alertes, pollutions, biodiversité, rapports, IoT, IA prédictive, logs, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, multilingue, extensibilité
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST environnement (sécurité, multilingue, souveraineté)
🇬🇧 Django REST environment routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للبيئة (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n tamenvrant (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'sites', views.SiteViewSet, basename='site')
router.register(r'capteurs', views.CapteurViewSet, basename='capteur')
router.register(r'mesures', views.MesureViewSet, basename='mesure')
router.register(r'alertes', views.AlerteViewSet, basename='alerte')
router.register(r'pollutions', views.PollutionViewSet, basename='pollution')
router.register(r'biodiversite', views.BiodiversiteViewSet, basename='biodiversite')
router.register(r'rapports', views.RapportViewSet, basename='rapport')
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

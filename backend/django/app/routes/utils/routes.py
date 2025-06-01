"""
Dihya – Django Utils API Routes Ultra Avancé
--------------------------------------------
- Endpoints REST pour outils utilitaires : génération UUID, conversion formats, validation emails, monitoring, outils IA, notifications, logs, rapports, migration, backup/restore
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, anonymisation, multilingue, extensibilité, fallback IA open source
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST utils (sécurité, multilingue, souveraineté)
🇬🇧 Django REST utils routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للأدوات (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n ifecka (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'uuid', views.UUIDViewSet, basename='uuid')
router.register(r'conversion', views.ConversionViewSet, basename='conversion')
router.register(r'validate_email', views.ValidateEmailViewSet, basename='validate-email')
router.register(r'monitoring', views.MonitoringViewSet, basename='monitoring')
router.register(r'ia', views.IAUtilsViewSet, basename='ia-utils')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'logs', views.LogUtilsViewSet, basename='log-utils')
router.register(r'rapports', views.RapportViewSet, basename='rapport')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')
router.register(r'backup', views.BackupViewSet, basename='backup')
router.register(r'restore', views.RestoreViewSet, basename='restore')
router.register(r'migration', views.MigrationViewSet, basename='migration')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, anonymisation, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Fallback IA open source : tous les endpoints critiques disposent d’un fallback open source
# Extensible : ajoutez vos endpoints (conversion, IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

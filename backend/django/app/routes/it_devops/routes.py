"""
Dihya – Django IT & DevOps API Routes Ultra Avancé
--------------------------------------------------
- Endpoints REST pour serveurs, déploiements, pipelines CI/CD, monitoring, logs, incidents, scripts, inventaire, audits, IA Ops
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, multilingue, extensibilité, fallback open source
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST IT & DevOps (sécurité, multilingue, souveraineté)
🇬🇧 Django REST IT & DevOps routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST لتقنية المعلومات و DevOps (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n IT & DevOps (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'serveurs', views.ServeurViewSet, basename='serveur')
router.register(r'deploiements', views.DeploiementViewSet, basename='deploiement')
router.register(r'pipelines', views.PipelineViewSet, basename='pipeline')
router.register(r'monitoring', views.MonitoringViewSet, basename='monitoring')
router.register(r'logs', views.LogViewSet, basename='log')
router.register(r'incidents', views.IncidentViewSet, basename='incident')
router.register(r'scripts', views.ScriptViewSet, basename='script')
router.register(r'inventaire', views.InventaireViewSet, basename='inventaire')
router.register(r'iaops', views.IAOpsViewSet, basename='iaops')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Fallback open source : tous les endpoints critiques disposent d’un fallback open source (ex : Ansible, Bash, Python)
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

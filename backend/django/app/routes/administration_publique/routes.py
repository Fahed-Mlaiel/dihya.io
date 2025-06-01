"""
Dihya – Django Administration Publique API Routes Ultra Avancé
-------------------------------------------------------------
- Endpoints REST pour démarches, documents, usagers, agents, notifications, logs, audit
- Sécurité, RBAC, logs, conformité RGPD/NIS2, multilingue, extensibilité
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST administration publique (sécurité, multilingue, souveraineté)
🇬🇧 Django REST public administration routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للإدارة العمومية (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n administration publique (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'demarches', views.DemarcheViewSet, basename='demarche')
router.register(r'documents', views.DocumentViewSet, basename='document')
router.register(r'usagers', views.UsagerViewSet, basename='usager')
router.register(r'agents', views.AgentViewSet, basename='agent')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Extensible : ajoutez vos endpoints (interop, open data, génération IA, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

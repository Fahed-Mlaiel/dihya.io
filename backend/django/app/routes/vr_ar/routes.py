"""
Dihya – Django VR/AR API Routes Ultra Avancé
--------------------------------------------
- Endpoints REST pour scènes, assets 3D, expériences, utilisateurs, analytics, IA VR/AR, notifications, logs, rapports, modération, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, anonymisation, modération IA, multilingue, extensibilité, fallback IA open source
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST VR/AR (sécurité, multilingue, souveraineté)
🇬🇧 Django REST VR/AR routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للواقع الافتراضي والمعزز (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n VR/AR (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'scenes', views.SceneViewSet, basename='scene')
router.register(r'assets', views.Asset3DViewSet, basename='asset-3d')
router.register(r'experiences', views.ExperienceViewSet, basename='experience')
router.register(r'utilisateurs', views.UtilisateurVRARViewSet, basename='utilisateur-vrar')
router.register(r'analytics', views.AnalyticsViewSet, basename='analytics')
router.register(r'ia', views.IAVRARViewSet, basename='ia-vrar')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'moderation', views.ModerationVRARViewSet, basename='moderation-vrar')
router.register(r'logs', views.LogVRARViewSet, basename='log-vrar')
router.register(r'rapports', views.RapportViewSet, basename='rapport')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, anonymisation, modération IA, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Fallback IA open source : tous les endpoints critiques disposent d’un fallback open source
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

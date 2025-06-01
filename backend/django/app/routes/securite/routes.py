"""
Dihya – Django Sécurité API Routes Ultra Avancé
-----------------------------------------------
- Endpoints REST pour utilisateurs, rôles, permissions, MFA, biométrie, logs, audit, alertes, IA sécurité, détection d’intrusion, conformité RGPD/NIS2
- Sécurité, RBAC, logs, chiffrement, MFA, biométrie, détection d’intrusion, alertes, anonymisation, multilingue, extensibilité, fallback IA open source
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST sécurité (sécurité, multilingue, souveraineté)
🇬🇧 Django REST security routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للأمان (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n tɣellist (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'utilisateurs', views.UtilisateurViewSet, basename='utilisateur')
router.register(r'roles', views.RoleViewSet, basename='role')
router.register(r'permissions', views.PermissionViewSet, basename='permission')
router.register(r'mfa', views.MFAViewSet, basename='mfa')
router.register(r'biometrie', views.BiometrieViewSet, basename='biometrie')
router.register(r'logs', views.LogSecuriteViewSet, basename='log-securite')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')
router.register(r'alertes', views.AlerteViewSet, basename='alerte')
router.register(r'ia', views.IASecuriteViewSet, basename='ia-securite')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'rapports', views.RapportViewSet, basename='rapport')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, MFA, biométrie, logs, chiffrement, détection d’intrusion, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Fallback IA open source : tous les endpoints critiques disposent d’un fallback open source
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

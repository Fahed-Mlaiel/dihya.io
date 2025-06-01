"""
Dihya – Django Mobile API Routes Ultra Avancé
---------------------------------------------
- Endpoints REST pour utilisateurs, profils, notifications push, médias, géolocalisation, synchronisation, IA mobile, logs, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, MFA, biométrie, multilingue, extensibilité, fallback IA open source
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST mobile (sécurité, multilingue, souveraineté)
🇬🇧 Django REST mobile routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للجوال (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n mobile (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'utilisateurs', views.UtilisateurViewSet, basename='utilisateur')
router.register(r'profils', views.ProfilViewSet, basename='profil')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'medias', views.MediaViewSet, basename='media')
router.register(r'geolocalisation', views.GeolocalisationViewSet, basename='geolocalisation')
router.register(r'synchronisation', views.SynchronisationViewSet, basename='synchronisation')
router.register(r'ia', views.IAMobileViewSet, basename='ia-mobile')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, MFA, biométrie, logs, chiffrement, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Fallback IA open source : tous les endpoints critiques disposent d’un fallback open source
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

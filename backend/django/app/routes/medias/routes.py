"""
Dihya – Django Médias API Routes Ultra Avancé
---------------------------------------------
- Endpoints REST pour fichiers, images, vidéos, audio, documents, tags, conversions, IA médias, streaming, publication, modération, logs, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, filigrane, DRM open source, multilingue, extensibilité
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST médias (sécurité, multilingue, souveraineté)
🇬🇧 Django REST media routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للإعلام (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n imedyazen (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'fichiers', views.FichierViewSet, basename='fichier')
router.register(r'images', views.ImageViewSet, basename='image')
router.register(r'videos', views.VideoViewSet, basename='video')
router.register(r'audio', views.AudioViewSet, basename='audio')
router.register(r'documents', views.DocumentViewSet, basename='document')
router.register(r'tags', views.TagViewSet, basename='tag')
router.register(r'conversions', views.ConversionViewSet, basename='conversion')
router.register(r'ia', views.IAMediasViewSet, basename='ia-medias')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, filigrane, DRM open source, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Fallback IA open source : tous les endpoints critiques disposent d’un fallback open source
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

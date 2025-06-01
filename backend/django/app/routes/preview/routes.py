"""
Dihya – Django Preview API Routes Ultra Avancé
----------------------------------------------
- Endpoints REST pour preview de documents, images, vidéos, audio, pages web, données, IA preview, conversion, streaming, logs, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, filigrane, multilingue, extensibilité, fallback IA open source
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST preview (sécurité, multilingue, souveraineté)
🇬🇧 Django REST preview routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للمعاينة (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n preview (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'documents', views.DocumentPreviewViewSet, basename='document-preview')
router.register(r'images', views.ImagePreviewViewSet, basename='image-preview')
router.register(r'videos', views.VideoPreviewViewSet, basename='video-preview')
router.register(r'audio', views.AudioPreviewViewSet, basename='audio-preview')
router.register(r'pages', views.PagePreviewViewSet, basename='page-preview')
router.register(r'donnees', views.DonneePreviewViewSet, basename='donnee-preview')
router.register(r'conversions', views.ConversionViewSet, basename='conversion')
router.register(r'ia', views.IAPreviewViewSet, basename='ia-preview')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, filigrane, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Fallback IA open source : tous les endpoints critiques disposent d’un fallback open source
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

"""
Dihya – Django 3D API Routes Ultra Avancé
-----------------------------------------
- Endpoints REST pour upload, conversion, visualisation, gestion et audit des assets 3D
- Sécurité, RBAC, logs, conformité RGPD/NIS2, multilingue, extensibilité
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST 3D (sécurité, multilingue, souveraineté)
🇬🇧 Django REST 3D routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST ثلاثية الأبعاد (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST 3D (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'upload', views.Model3DUploadViewSet, basename='3d-upload')
router.register(r'convert', views.Model3DConvertViewSet, basename='3d-convert')
router.register(r'preview', views.Model3DPreviewViewSet, basename='3d-preview')
router.register(r'assets', views.Model3DAssetViewSet, basename='3d-assets')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Extensible : ajoutez vos endpoints (analyse IA, génération, watermark, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SceneViewSet, AssetViewSet

router = DefaultRouter()
router.register(r'scenes', SceneViewSet, basename='vr_ar-scene')
router.register(r'assets', AssetViewSet, basename='vr_ar-asset')

urlpatterns = [
    path('', include(router.urls)),
    # Endpoint RGPD export (à implémenter dans views avancées)
    # path('rgpd-export/', ... , name='vr_ar-rgpd-export'),
]

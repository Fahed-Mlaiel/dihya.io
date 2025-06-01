from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AudioFileViewSet, TranscriptionViewSet

router = DefaultRouter()
router.register(r'audiofiles', AudioFileViewSet, basename='voice-audiofile')
router.register(r'transcriptions', TranscriptionViewSet, basename='voice-transcription')

urlpatterns = [
    path('', include(router.urls)),
    # Endpoint RGPD export (à implémenter dans views.py)
    path('rgpd-export/', lambda request: None, name='voice-rgpd-export'),
]

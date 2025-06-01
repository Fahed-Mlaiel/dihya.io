"""
Dihya – Django Voice API Routes Ultra Avancé
--------------------------------------------
- Endpoints REST pour transcription, synthèse vocale (TTS), reconnaissance vocale (ASR), analyse audio, traduction, modération IA, notifications, logs, rapports, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, anonymisation, modération IA, multilingue, extensibilité, fallback IA open source
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST voice (sécurité, multilingue, souveraineté)
🇬🇧 Django REST voice routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للصوت (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n imesli (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'transcription', views.TranscriptionViewSet, basename='transcription')
router.register(r'tts', views.TTSViewSet, basename='tts')
router.register(r'asr', views.ASRViewSet, basename='asr')
router.register(r'analyse', views.AnalyseAudioViewSet, basename='analyse-audio')
router.register(r'traduction', views.TraductionAudioViewSet, basename='traduction-audio')
router.register(r'moderation', views.ModerationAudioViewSet, basename='moderation-audio')
router.register(r'ia', views.IAVoiceViewSet, basename='ia-voice')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'logs', views.LogVoiceViewSet, basename='log-voice')
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

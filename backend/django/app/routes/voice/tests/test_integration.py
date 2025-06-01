# Test d’intégration pour le module voice
# Vérifie l’intégration entre upload, transcription, audit et RGPD.

import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from ..models import AudioFile, Transcription
from ..audit import voice_audit_logger

@pytest.mark.django_db
def test_voice_integration_audit_rgpd():
    client = APIClient()
    user = get_user_model().objects.create_user(username='intuser', password='pass')
    client.force_authenticate(user=user)
    # Upload
    with open('assets/audio_en.mp3', 'rb') as audio:
        response = client.post(reverse('voice-audiofile-list'), {'file': audio, 'language': 'en'})
        assert response.status_code == 201
        audio_id = response.data['id']
    # Transcription
    response = client.post(reverse('voice-transcription-list'), {'audio_file': audio_id, 'language': 'en'})
    assert response.status_code == 201
    transcription_id = response.data['id']
    # Audit
    voice_audit_logger.log(user, 'test_audit', 'AudioFile', audio_id, details='Test integration', language='en')
    # RGPD Export
    response = client.get(reverse('voice-rgpd-export'))
    assert response.status_code == 200
    assert 'application/json' in response['Content-Type']

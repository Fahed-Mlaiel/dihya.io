# Test e2e pour le module voice
# Scénario complet : upload, transcription, export RGPD, suppression.

import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model

@pytest.mark.django_db
def test_voice_e2e_workflow():
    client = APIClient()
    user = get_user_model().objects.create_user(username='e2euser', password='pass')
    client.force_authenticate(user=user)
    # Upload
    with open('assets/audio_fr.mp3', 'rb') as audio:
        response = client.post(reverse('voice-audiofile-list'), {'file': audio, 'language': 'fr'})
        assert response.status_code == 201
        audio_id = response.data['id']
    # Transcription
    response = client.post(reverse('voice-transcription-list'), {'audio_file': audio_id, 'language': 'fr'})
    assert response.status_code == 201
    transcription_id = response.data['id']
    # Export RGPD
    response = client.get(reverse('voice-rgpd-export'))
    assert response.status_code == 200
    # Suppression
    response = client.delete(reverse('voice-audiofile-detail', args=[audio_id]))
    assert response.status_code in [204, 200]

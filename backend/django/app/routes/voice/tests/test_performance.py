# Test de performance pour le module voice
# Mesure le temps d’upload et de transcription d’un fichier audio.

import pytest
import time
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model

@pytest.mark.django_db
def test_audiofile_upload_performance():
    client = APIClient()
    user = get_user_model().objects.create_user(username='perfuser', password='pass')
    client.force_authenticate(user=user)
    with open('assets/audio_fr.mp3', 'rb') as audio:
        start = time.time()
        response = client.post(reverse('voice-audiofile-list'), {'file': audio, 'language': 'fr'})
        duration = time.time() - start
    assert response.status_code == 201
    assert duration < 2  # L’upload doit être rapide

@pytest.mark.django_db
def test_transcription_performance():
    client = APIClient()
    user = get_user_model().objects.create_user(username='perfuser2', password='pass')
    client.force_authenticate(user=user)
    from ..models import AudioFile
    audio = AudioFile.objects.create(file='assets/audio_fr.mp3', language='fr', uploaded_by=user)
    start = time.time()
    response = client.post(reverse('voice-transcription-list'), {'audio_file': audio.id, 'language': 'fr'})
    duration = time.time() - start
    assert response.status_code == 201
    assert duration < 3  # La transcription doit être rapide

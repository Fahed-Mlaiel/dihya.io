import sys
sys.path.insert(0, '.')
from backend.django.app.routes.voice.models import AudioFile, Transcription
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

@pytest.mark.django_db
def test_upload_audiofile_fr():
    client = APIClient()
    user = get_user_model().objects.create_user(username='userfr', password='pass')
    client.force_authenticate(user=user)
    with open('assets/audio_fr.mp3', 'rb') as audio:
        response = client.post(reverse('voice-audiofile-list'), {'file': audio, 'language': 'fr'})
    assert response.status_code == 201
    assert AudioFile.objects.filter(language='fr').exists()

@pytest.mark.django_db
def test_transcription_arabic():
    client = APIClient()
    user = get_user_model().objects.create_user(username='userar', password='pass')
    client.force_authenticate(user=user)
    audio = AudioFile.objects.create(file='assets/audio_ar.mp3', language='ar', uploaded_by=user)
    response = client.post(reverse('voice-transcription-list'), {'audio_file': audio.id, 'language': 'ar'})
    assert response.status_code == 201
    assert Transcription.objects.filter(audio_file=audio, language='ar').exists()

@pytest.mark.django_db
def test_permission_denied():
    client = APIClient()
    user1 = get_user_model().objects.create_user(username='user1', password='pass')
    user2 = get_user_model().objects.create_user(username='user2', password='pass')
    client.force_authenticate(user=user2)
    audio = AudioFile.objects.create(file='assets/audio_en.mp3', language='en', uploaded_by=user1)
    response = client.delete(reverse('voice-audiofile-detail', args=[audio.id]))
    assert response.status_code == 403

@pytest.mark.django_db
def test_rgpd_export():
    client = APIClient()
    user = get_user_model().objects.create_user(username='userrgpd', password='pass')
    client.force_authenticate(user=user)
    # Simuler endpoint d'export RGPD (à implémenter dans views.py)
    response = client.get(reverse('voice-rgpd-export'))
    assert response.status_code == 200
    assert 'application/json' in response['Content-Type']

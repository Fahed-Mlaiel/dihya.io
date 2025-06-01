# Test unitaire avancé pour le plugin d’analyse de sentiment du module voice

import pytest
from ..plugins import analyse_sentiment
from ..models import Transcription
from django.contrib.auth import get_user_model

@pytest.mark.django_db
def test_analyse_sentiment_neutre():
    user = get_user_model().objects.create_user(username='sentineutre', password='pass')
    tr = Transcription.objects.create(audio_file_id=1, text='Ceci est un test.', language='fr')
    assert analyse_sentiment(tr.id) == 'neutre'

@pytest.mark.django_db
def test_analyse_sentiment_positif():
    user = get_user_model().objects.create_user(username='sentipos', password='pass')
    tr = Transcription.objects.create(audio_file_id=2, text='Bravo pour ce résultat !', language='fr')
    assert analyse_sentiment(tr.id) == 'positif'

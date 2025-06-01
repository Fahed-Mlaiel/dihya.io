# Script Python d'import de fixtures audio pour le module voice
# Usage: python import_fixtures.py
# Importe les fichiers audio et transcriptions depuis fixtures.json

import json
from django.core.management.base import BaseCommand
from ...models import AudioFile, Transcription
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Importe les fixtures audio et transcription pour le module voice.'

    def handle(self, *args, **kwargs):
        with open('fixtures.json', 'r') as f:
            data = json.load(f)
        for audio in data['audiofiles']:
            user = get_user_model().objects.get(id=audio['uploaded_by'])
            AudioFile.objects.get_or_create(
                id=audio['id'],
                file=audio['file'],
                language=audio['language'],
                uploaded_by=user
            )
        for tr in data['transcriptions']:
            audiofile = AudioFile.objects.get(id=tr['audio_file'])
            Transcription.objects.get_or_create(
                id=tr['id'],
                audio_file=audiofile,
                text=tr['text'],
                language=tr['language']
            )
        self.stdout.write(self.style.SUCCESS('Fixtures importées avec succès.'))

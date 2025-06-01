# Script Python d'import de fixtures pour le module vr_ar
# Usage: python import_fixtures.py
# Importe les scènes et assets depuis fixtures.json

import json
from django.core.management.base import BaseCommand
from ...models import Scene, Asset
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Importe les fixtures de scènes et assets pour le module vr_ar.'

    def handle(self, *args, **kwargs):
        with open('fixtures.json', 'r') as f:
            data = json.load(f)
        for scene in data['scenes']:
            user = get_user_model().objects.get(id=scene['created_by'])
            Scene.objects.get_or_create(
                id=scene['id'],
                title=scene['title'],
                description=scene['description'],
                lang=scene['lang'],
                created_by=user,
                created_at=scene['created_at']
            )
        for asset in data['assets']:
            scene_obj = Scene.objects.get(id=asset['scene'])
            Asset.objects.get_or_create(
                id=asset['id'],
                scene=scene_obj,
                file=asset['file'],
                type=asset['type'],
                lang=asset['lang']
            )
        self.stdout.write(self.style.SUCCESS('Fixtures importées avec succès.'))

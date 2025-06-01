# Script Python d'import de fixtures pour le module voyage
# Usage: python import_fixtures.py
# Importe les réservations et itinéraires depuis fixtures.json

import json
from django.core.management.base import BaseCommand
from ...models import Reservation, Itineraire
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Importe les fixtures de réservation et itinéraire pour le module voyage.'

    def handle(self, *args, **kwargs):
        with open('fixtures.json', 'r') as f:
            data = json.load(f)
        for itin in data['itineraires']:
            Itineraire.objects.get_or_create(
                id=itin['id'],
                depart=itin['depart'],
                arrivee=itin['arrivee'],
                distance_km=itin['distance_km']
            )
        for res in data['reservations']:
            user = get_user_model().objects.get(id=res['user'])
            Reservation.objects.get_or_create(
                id=res['id'],
                user=user,
                voyage=res['voyage'],
                date=res['date'],
                status=res['status'],
                lang=res['lang']
            )
        self.stdout.write(self.style.SUCCESS('Fixtures importées avec succès.'))

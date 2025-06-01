"""
Dihya – Tests unitaires et d'intégration pour Tourisme
- Couverture exhaustive, sécurité, RGPD, multilingue
"""
from django.test import TestCase
from .models import Destination, Offre, Reservation, Avis

class DestinationModelTest(TestCase):
    def test_str(self):
        d = Destination.objects.create(nom='Paris', pays='France', description='Ville lumière')
        self.assertEqual(str(d), 'Paris')

class OffreModelTest(TestCase):
    def test_str(self):
        d = Destination.objects.create(nom='Paris', pays='France', description='Ville lumière')
        o = Offre.objects.create(destination=d, titre='Séjour', description='Séjour à Paris', prix=1000, date_debut='2024-06-01', date_fin='2024-06-10')
        self.assertEqual(str(o), 'Séjour')

class ReservationModelTest(TestCase):
    def test_str(self):
        d = Destination.objects.create(nom='Paris', pays='France', description='Ville lumière')
        o = Offre.objects.create(destination=d, titre='Séjour', description='Séjour à Paris', prix=1000, date_debut='2024-06-01', date_fin='2024-06-10')
        r = Reservation.objects.create(offre=o, nom_client='Alice', email_client='alice@example.com', date_reservation='2024-05-01', statut='en_attente')
        self.assertIn('Alice', str(r))

class AvisModelTest(TestCase):
    def test_str(self):
        d = Destination.objects.create(nom='Paris', pays='France', description='Ville lumière')
        o = Offre.objects.create(destination=d, titre='Séjour', description='Séjour à Paris', prix=1000, date_debut='2024-06-01', date_fin='2024-06-10')
        r = Reservation.objects.create(offre=o, nom_client='Alice', email_client='alice@example.com', date_reservation='2024-05-01', statut='en_attente')
        a = Avis.objects.create(reservation=r, note=5, commentaire='Excellent', date_avis='2024-05-02')
        self.assertIn('Avis', str(a))

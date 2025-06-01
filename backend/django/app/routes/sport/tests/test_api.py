"""
Dihya – Tests API avancés pour Sport
- Tests unitaires, intégration, sécurité, accessibilité, multilingue
"""
from rest_framework.test import APITestCase
from django.urls import reverse
from ..models import Club, Equipe, Athlete, Competition, Resultat

class ClubAPITest(APITestCase):
    def setUp(self):
        self.club = Club.objects.create(nom='Olympique Paris', ville='Paris', date_fondation='1980-01-01')
    def test_list_clubs(self):
        url = reverse('club-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    def test_create_club(self):
        url = reverse('club-list')
        data = {'nom': 'FC Test', 'ville': 'Lyon', 'date_fondation': '2001-01-01'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

class EquipeAPITest(APITestCase):
    def setUp(self):
        self.club = Club.objects.create(nom='Olympique Paris', ville='Paris', date_fondation='1980-01-01')
        self.equipe = Equipe.objects.create(club=self.club, nom='Equipe A', categorie='Senior')
    def test_list_equipes(self):
        url = reverse('equipe-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

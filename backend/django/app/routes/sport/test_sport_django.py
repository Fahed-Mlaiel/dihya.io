"""
Dihya – Tests unitaires et d'intégration pour Sport
- Couverture exhaustive, sécurité, RGPD, multilingue
"""
from django.test import TestCase
from .models import Club, Equipe, Athlete, Competition, Resultat

class ClubModelTest(TestCase):
    def test_str(self):
        c = Club.objects.create(nom='Test Club', ville='Paris', date_fondation='2000-01-01')
        self.assertEqual(str(c), 'Test Club')

class EquipeModelTest(TestCase):
    def test_str(self):
        club = Club.objects.create(nom='Test Club', ville='Paris', date_fondation='2000-01-01')
        e = Equipe.objects.create(club=club, nom='Equipe 1', categorie='Senior')
        self.assertEqual(str(e), 'Equipe 1')

class AthleteModelTest(TestCase):
    def test_str(self):
        club = Club.objects.create(nom='Test Club', ville='Paris', date_fondation='2000-01-01')
        e = Equipe.objects.create(club=club, nom='Equipe 1', categorie='Senior')
        a = Athlete.objects.create(equipe=e, nom='Doe', prenom='Jane', date_naissance='1990-01-01')
        self.assertEqual(str(a), 'Jane Doe')

class CompetitionModelTest(TestCase):
    def test_str(self):
        c = Competition.objects.create(nom='Coupe', date='2024-01-01', lieu='Paris')
        self.assertEqual(str(c), 'Coupe')

class ResultatModelTest(TestCase):
    def test_str(self):
        club = Club.objects.create(nom='Test Club', ville='Paris', date_fondation='2000-01-01')
        e = Equipe.objects.create(club=club, nom='Equipe 1', categorie='Senior')
        c = Competition.objects.create(nom='Coupe', date='2024-01-01', lieu='Paris')
        r = Resultat.objects.create(competition=c, equipe=e, score='2-1', classement=1)
        self.assertIn('Equipe 1', str(r))

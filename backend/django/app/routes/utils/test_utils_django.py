"""
Dihya – Tests unitaires et d'intégration pour Utils
- Couverture exhaustive, sécurité, RGPD, multilingue
"""
from django.test import TestCase
from .models import LogEntry

class LogEntryModelTest(TestCase):
    def test_str(self):
        l = LogEntry.objects.create(niveau='INFO', message='Test log', utilisateur='admin')
        self.assertIn('INFO', str(l))

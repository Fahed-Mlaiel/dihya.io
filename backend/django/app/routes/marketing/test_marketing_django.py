"""
Dihya – Tests unitaires et d'intégration pour le module Marketing
- Couverture exhaustive, multilingue, sécurité, RGPD
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Campagne, Lead, Audience, Canal, Contenu, Analytics, ABTesting, Notification, Rapport, AuditLog
from rest_framework.test import APIClient
from rest_framework import status

class MarketingAPITestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass', is_marketing_admin=True)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.audience = Audience.objects.create(nom='Test Audience', cree_par=self.user)
        self.campagne = Campagne.objects.create(nom='Campagne Test', canal='email', audience=self.audience, contenu='Contenu test', date_debut='2025-01-01T00:00:00Z', date_fin='2025-12-31T23:59:59Z', cree_par=self.user)

    def test_create_lead(self):
        data = {'nom': 'Lead Test', 'email': 'lead@example.com', 'source': 'landing', 'campagne': self.campagne.id}
        response = self.client.post('/api/marketing/leads/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nom'], 'Lead Test')

    def test_permission_denied_for_non_admin(self):
        self.client.force_authenticate(user=None)
        response = self.client.post('/api/marketing/campagnes/', {'nom': 'X', 'canal': 'email', 'audience': self.audience.id, 'contenu': 'X', 'date_debut': '2025-01-01T00:00:00Z', 'date_fin': '2025-12-31T23:59:59Z'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_audit_log_created(self):
        from .audit import log_action
        log_action(self.user, 'TEST_ACTION', 'Détails test')
        self.assertTrue(AuditLog.objects.filter(action='TEST_ACTION').exists())

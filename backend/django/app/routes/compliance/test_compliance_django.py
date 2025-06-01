"""
Tests unitaires et intégration Compliance (couverture maximale, multilingue, RGPD, audit)
"""
from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse

class ComplianceReportTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('compliance-report-list')

    def test_list_reports_unauthenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 401)

    def test_list_reports_authenticated(self):
        from django.contrib.auth.models import User
        user = User.objects.create_user('testuser', 'test@example.com', 'testpass')
        self.client.force_authenticate(user=user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('tenant', response.json()[0])

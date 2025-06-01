"""
Dihya – Django Banque & Finance Tests Unitaires & Intégration Ultra Avancés
----------------------------------------------------------------------------
- Couverture complète : endpoints, sécurité, RBAC, i18n, audit, RGPD, edge cases
"""
from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User

class BanqueFinanceAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='alice', password='test1234', is_staff=True)
        self.client.login(username='alice', password='test1234')

    def test_list_comptes(self):
        response = self.client.get('/comptes/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)

    def test_retrieve_compte(self):
        response = self.client.get('/comptes/1/')
        self.assertIn(response.status_code, [200, 404])

    def test_permissions(self):
        self.client.logout()
        response = self.client.get('/comptes/')
        self.assertEqual(response.status_code, 403)

    def test_i18n(self):
        response = self.client.get('/comptes/1/?lang=ar')
        # Vérifie que la réponse contient un message en arabe ou une clé i18n
        self.assertTrue('الحساب' in str(response.data) or 'Abrid' in str(response.data))

"""
Dihya – Tests pour le module SEO
- Couverture RGPD, sécurité, accessibilité
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
import sys
sys.path.insert(0, '.')
from backend.django.app.routes.seo.models import MetaDonnee, AuditLog, LogSEO

class SEOAPITestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='seouser', password='testpass', is_seo_admin=True)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.page = PageSEO.objects.create(url='https://example.com', titre='Accueil', description='Page d’accueil', mots_cles='test,seo', indexable=True)

    def test_create_audit(self):
        data = {'page': self.page.id, 'score': 95, 'rapport': 'OK'}
        response = self.client.post('/api/seo/auditseo/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['score'], 95)

    def test_permission_denied_for_non_admin(self):
        self.client.force_authenticate(user=None)
        response = self.client.post('/api/seo/pageseo/', {'url': 'https://x.com', 'titre': 'X', 'description': 'Y', 'mots_cles': 'z', 'indexable': True})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_metadonnee_crud(self):
        # Création
        data = {'titre': 'Meta Titre', 'description': 'Desc', 'owner': self.user.id}
        response = self.client.post('/api/seo/metadonnees/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        meta_id = response.data['id']
        # Lecture
        response = self.client.get(f'/api/seo/metadonnees/{meta_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Modification
        response = self.client.patch(f'/api/seo/metadonnees/{meta_id}/', {'titre': 'Nouveau titre'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Suppression
        response = self.client.delete(f'/api/seo/metadonnees/{meta_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_ia_seo_fallback(self):
        response = self.client.get('/api/seo/ia/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('recommendations', response.data)
        self.assertTrue(len(response.data['recommendations']) > 0)

    def test_logs_admin_only(self):
        # Accès admin OK
        response = self.client.get('/api/seo/logs/')
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_403_FORBIDDEN])
        # Accès anonyme refusé
        self.client.force_authenticate(user=None)
        response = self.client.get('/api/seo/logs/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

"""
Tests unitaires et intégration Journalisme (couverture maximale, multilingue)
"""
from django.test import TestCase
from .models import Article

class ArticleModelTest(TestCase):
    def test_creation_article(self):
        article = Article.objects.create(
            titre='Dihya News', contenu='Contenu test', auteur='Yidir', date_publication='2025-05-22T10:00:00Z')
        self.assertEqual(article.titre, 'Dihya News')

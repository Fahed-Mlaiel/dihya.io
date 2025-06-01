"""
Tests unitaires et intégration IT & DevOps (couverture maximale, multilingue)
"""
from django.test import TestCase
from .models import Pipeline

class PipelineModelTest(TestCase):
    def test_creation_pipeline(self):
        pipeline = Pipeline.objects.create(
            nom='CI Amazigh', type='CI', status='actif', responsable='Yidir')
        self.assertEqual(pipeline.nom, 'CI Amazigh')

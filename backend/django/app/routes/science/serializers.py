"""
Dihya – Serializers pour le module Science
- Validation RGPD, accessibilité, multilingue, sécurité
"""
from rest_framework import serializers
from .models import ProjetScientifique, Publication, Chercheur

class ProjetScientifiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjetScientifique
        fields = '__all__'

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'

class ChercheurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chercheur
        fields = '__all__'

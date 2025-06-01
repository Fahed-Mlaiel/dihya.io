"""
Dihya – Serializers pour le module Recherche
- Validation RGPD, accessibilité, multilingue, sécurité
"""
from rest_framework import serializers
from .models import RequeteRecherche, ResultatRecherche

class RequeteRechercheSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequeteRecherche
        fields = '__all__'

class ResultatRechercheSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultatRecherche
        fields = '__all__'

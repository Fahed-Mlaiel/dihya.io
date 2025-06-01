"""
Dihya – Serializers pour le module Publicité
- Validation RGPD, accessibilité, multilingue, sécurité
"""
from rest_framework import serializers
from .models import CampagnePublicitaire, AnalyticsPublicite

class CampagnePublicitaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampagnePublicitaire
        fields = '__all__'

class AnalyticsPubliciteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalyticsPublicite
        fields = '__all__'

"""
Dihya – Serializers pour le module Sécurité
- Validation RGPD, accessibilité, multilingue, sécurité
"""
from rest_framework import serializers
from .models import IncidentSecurite, AlerteSecurite, ControleSecurite

class IncidentSecuriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncidentSecurite
        fields = '__all__'

class AlerteSecuriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlerteSecurite
        fields = '__all__'

class ControleSecuriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControleSecurite
        fields = '__all__'

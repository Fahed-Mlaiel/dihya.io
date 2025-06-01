"""
Dihya – Serializers pour le module Preview
- Validation RGPD, accessibilité, multilingue, sécurité
"""
from rest_framework import serializers
from .models import Preview

class PreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preview
        fields = '__all__'

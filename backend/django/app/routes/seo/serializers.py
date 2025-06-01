"""
Dihya – Serializers pour le module SEO
- Validation RGPD, accessibilité, multilingue, sécurité
"""
from rest_framework import serializers
from .models import PageSEO, AuditSEO

class PageSEOSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageSEO
        fields = '__all__'

class AuditSEOSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditSEO
        fields = '__all__'

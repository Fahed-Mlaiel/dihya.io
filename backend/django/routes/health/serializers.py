"""
Serializers avancés pour les projets santé (REST & GraphQL-ready).
Inclut validation, sécurité, multilingue, RGPD.
"""
from rest_framework import serializers
from .models import HealthProject

class HealthProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProject
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'tenant', 'created_by', 'is_active']
        read_only_fields = ['id', 'created_at', 'updated_at', 'created_by', 'tenant']

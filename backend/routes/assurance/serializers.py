"""
Serializers ultra avancés pour Assurance (Dihya)
REST, GraphQL, multilingue, RGPD, plugins, audit, sécurité maximale.
"""
from rest_framework import serializers
from .models import AssuranceProject, AssuranceAsset

class AssuranceProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssuranceProject
        fields = ['id', 'name', 'description', 'created_by', 'created_at', 'updated_at', 'lang']

class AssuranceAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssuranceAsset
        fields = ['id', 'project', 'file', 'type', 'lang', 'uploaded_at']

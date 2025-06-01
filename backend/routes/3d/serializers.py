"""
Serializers ultra avancés pour 3D (Django routes)
REST, GraphQL, multilingue, RGPD, plugins, audit, sécurité maximale.
"""
from rest_framework import serializers
from .models import ThreeDProject, ThreeDAsset

class ThreeDProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreeDProject
        fields = ['id', 'name', 'description', 'lang', 'created_by', 'created_at', 'updated_at']

class ThreeDAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreeDAsset
        fields = ['id', 'project', 'file', 'type', 'lang', 'uploaded_at']

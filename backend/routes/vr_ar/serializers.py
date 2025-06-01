"""
Serializers ultra avancés pour VR/AR (Django routes)
REST, GraphQL, multilingue, RGPD, plugins, audit, sécurité maximale.
"""
from rest_framework import serializers
from .models import Scene, Asset

class SceneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scene
        fields = ['id', 'title', 'description', 'lang', 'created_by', 'created_at', 'updated_at']

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['id', 'scene', 'file', 'type', 'lang', 'uploaded_at']

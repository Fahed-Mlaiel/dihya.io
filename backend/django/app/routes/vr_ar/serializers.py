from rest_framework import serializers
from .models import Scene, Asset

class SceneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scene
        fields = ['id', 'title', 'description', 'lang', 'created_by', 'created_at', 'updated_at']
        extra_kwargs = {
            'title': {'help_text': 'Titre de la scène VR/AR'},
            'description': {'help_text': 'Description de la scène'},
            'lang': {'help_text': 'Langue de la scène'}
        }

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['id', 'scene', 'file', 'type', 'lang', 'uploaded_at']
        extra_kwargs = {
            'file': {'help_text': 'Fichier 3D/VR/AR'},
            'type': {'help_text': 'Type d’asset'},
            'lang': {'help_text': 'Langue de l’asset'}
        }

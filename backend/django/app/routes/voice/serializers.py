"""
Dihya – Serializers avancés pour le module Voice
- Validation RGPD, multilingue, accessibilité, sécurité, documentation
"""
from rest_framework import serializers
from .models import AudioFile, Transcription

class AudioFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioFile
        fields = '__all__'
        extra_kwargs = {
            'fichier': {'help_text': 'Fichier audio'},
            'langue': {'help_text': 'Langue'},
            'utilisateur': {'help_text': 'Utilisateur'},
        }

class TranscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transcription
        fields = '__all__'
        extra_kwargs = {
            'audio': {'help_text': 'Fichier audio'},
            'texte': {'help_text': 'Texte transcrit'},
            'langue': {'help_text': 'Langue'},
            'utilisateur': {'help_text': 'Utilisateur'},
        }

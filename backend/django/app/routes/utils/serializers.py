"""
Dihya – Serializers utilitaires pour API Utils
- Pour logs, conversions, monitoring, etc.
"""
from rest_framework import serializers
from .models import LogEntry

class LogEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEntry
        fields = '__all__'
        extra_kwargs = {
            'niveau': {'help_text': 'Niveau du log'},
            'message': {'help_text': 'Message du log'},
            'utilisateur': {'help_text': 'Utilisateur'},
        }

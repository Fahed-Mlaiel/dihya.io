"""
Dihya – Serializers pour Validators
- Pour logs, schémas, validations, etc.
"""
from rest_framework import serializers
from .models import ValidationLog

class ValidationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValidationLog
        fields = '__all__'
        extra_kwargs = {
            'type_validation': {'help_text': 'Type de validation'},
            'resultat': {'help_text': 'Résultat'},
            'details': {'help_text': 'Détails'},
            'utilisateur': {'help_text': 'Utilisateur'},
        }

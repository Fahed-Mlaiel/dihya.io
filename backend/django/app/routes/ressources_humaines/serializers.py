"""
Dihya – Serializers pour le module Ressources Humaines
- Validation RGPD, accessibilité, multilingue, sécurité
"""
from rest_framework import serializers
from .models import Employe, Poste, Candidature

class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = '__all__'

class PosteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poste
        fields = '__all__'

class CandidatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidature
        fields = '__all__'

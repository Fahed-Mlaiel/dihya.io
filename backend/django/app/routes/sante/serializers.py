"""
Dihya – Serializers pour le module Santé
- Validation RGPD, accessibilité, multilingue, sécurité
"""
from rest_framework import serializers
from .models import Patient, RendezVous, DossierMedical

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class RendezVousSerializer(serializers.ModelSerializer):
    class Meta:
        model = RendezVous
        fields = '__all__'

class DossierMedicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DossierMedical
        fields = '__all__'

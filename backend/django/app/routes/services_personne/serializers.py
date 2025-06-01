"""
Dihya – Serializers avancés pour le module Services à la Personne
- Validation RGPD, multilingue, accessibilité, sécurité, documentation
"""
from rest_framework import serializers
from .models import Beneficiaire, Intervenant, Prestation

class BeneficiaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiaire
        fields = '__all__'
        extra_kwargs = {
            'nom': {'help_text': 'Nom du bénéficiaire'},
            'prenom': {'help_text': 'Prénom du bénéficiaire'},
            'email': {'help_text': 'Email du bénéficiaire'},
            'telephone': {'help_text': 'Téléphone'},
            'adresse': {'help_text': 'Adresse'},
        }

class IntervenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intervenant
        fields = '__all__'
        extra_kwargs = {
            'nom': {'help_text': 'Nom de l’intervenant'},
            'prenom': {'help_text': 'Prénom de l’intervenant'},
            'email': {'help_text': 'Email de l’intervenant'},
            'specialite': {'help_text': 'Spécialité'},
        }

class PrestationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestation
        fields = '__all__'
        extra_kwargs = {
            'beneficiaire': {'help_text': 'Bénéficiaire'},
            'intervenant': {'help_text': 'Intervenant'},
            'type_prestation': {'help_text': 'Type de prestation'},
            'date': {'help_text': 'Date de la prestation'},
            'statut': {'help_text': 'Statut de la prestation'},
        }

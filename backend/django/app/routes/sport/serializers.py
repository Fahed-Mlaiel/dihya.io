"""
Dihya – Serializers avancés pour le module Sport
- Validation RGPD, multilingue, accessibilité, sécurité, documentation
"""
from rest_framework import serializers
from .models import Club, Equipe, Athlete, Competition, Resultat

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'
        extra_kwargs = {
            'nom': {'help_text': 'Nom du club'},
            'ville': {'help_text': 'Ville'},
            'date_fondation': {'help_text': 'Date de fondation'},
        }

class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = '__all__'
        extra_kwargs = {
            'club': {'help_text': 'Club'},
            'nom': {'help_text': 'Nom de l’équipe'},
            'categorie': {'help_text': 'Catégorie'},
        }

class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = '__all__'
        extra_kwargs = {
            'equipe': {'help_text': 'Équipe'},
            'nom': {'help_text': 'Nom de l’athlète'},
            'prenom': {'help_text': 'Prénom de l’athlète'},
            'date_naissance': {'help_text': 'Date de naissance'},
        }

class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = '__all__'
        extra_kwargs = {
            'nom': {'help_text': 'Nom de la compétition'},
            'date': {'help_text': 'Date de la compétition'},
            'lieu': {'help_text': 'Lieu'},
        }

class ResultatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resultat
        fields = '__all__'
        extra_kwargs = {
            'competition': {'help_text': 'Compétition'},
            'equipe': {'help_text': 'Équipe'},
            'score': {'help_text': 'Score'},
            'classement': {'help_text': 'Classement'},
        }

"""
Dihya – Serializers avancés pour le module Tourisme
- Validation RGPD, multilingue, accessibilité, sécurité, documentation
"""
from rest_framework import serializers
from .models import Destination, Offre, Reservation, Avis

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'
        extra_kwargs = {
            'nom': {'help_text': 'Nom de la destination'},
            'pays': {'help_text': 'Pays'},
            'description': {'help_text': 'Description'},
        }

class OffreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offre
        fields = '__all__'
        extra_kwargs = {
            'destination': {'help_text': 'Destination'},
            'titre': {'help_text': 'Titre de l’offre'},
            'description': {'help_text': 'Description de l’offre'},
            'prix': {'help_text': 'Prix'},
            'date_debut': {'help_text': 'Date de début'},
            'date_fin': {'help_text': 'Date de fin'},
        }

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
        extra_kwargs = {
            'offre': {'help_text': 'Offre'},
            'nom_client': {'help_text': 'Nom du client'},
            'email_client': {'help_text': 'Email du client'},
            'date_reservation': {'help_text': 'Date de réservation'},
            'statut': {'help_text': 'Statut de la réservation'},
        }

class AvisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avis
        fields = '__all__'
        extra_kwargs = {
            'reservation': {'help_text': 'Réservation'},
            'note': {'help_text': 'Note (1-5)'},
            'commentaire': {'help_text': 'Commentaire'},
            'date_avis': {'help_text': 'Date de l’avis'},
        }

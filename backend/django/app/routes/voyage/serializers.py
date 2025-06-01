from rest_framework import serializers
from .models import Reservation, Itineraire

class ItineraireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itineraire
        fields = ['id', 'depart', 'arrivee', 'distance_km']
        extra_kwargs = {
            'depart': {'help_text': 'Ville de départ'},
            'arrivee': {'help_text': "Ville d'arrivée"},
            'distance_km': {'help_text': 'Distance en kilomètres'}
        }

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'user', 'voyage', 'date', 'status', 'lang', 'created_at', 'updated_at']
        extra_kwargs = {
            'voyage': {'help_text': 'Nom du voyage ou itinéraire'},
            'status': {'help_text': 'Statut de la réservation'},
            'lang': {'help_text': 'Langue de la réservation'}
        }

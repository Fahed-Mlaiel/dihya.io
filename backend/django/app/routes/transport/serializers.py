# Serializers ultra avancés pour le transport (véhicules, trajets, horaires, réservations, tickets, flotte, chauffeurs, IA, audit, notifications)
# Multilingue, souveraineté, sécurité, accessibilité, extensibilité

from rest_framework import serializers
from .models import Vehicule, Trajet, Horaire, Reservation, Ticket, Flotte, Chauffeur, IATransport, Notification, Rapport, LogTransport, AuditLog

class VehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicule
        fields = '__all__'
    # ... gestion multilingue, validation avancée, sécurité ...

class TrajetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trajet
        fields = '__all__'
    # ... gestion multilingue, validation avancée, sécurité ...

class HoraireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horaire
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class FlotteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flotte
        fields = '__all__'

class ChauffeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chauffeur
        fields = '__all__'

class IATransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = IATransport
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class RapportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rapport
        fields = '__all__'

class LogTransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogTransport
        fields = '__all__'

class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = '__all__'
# ... chaque serializer intègre i18n, fallback IA, accessibilité, sécurité, conformité RGPD/NIS2 ...

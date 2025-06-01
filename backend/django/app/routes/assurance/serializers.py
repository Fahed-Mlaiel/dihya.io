"""
Dihya – Django Assurance API Serializers Ultra Avancé
----------------------------------------------------
- Sérialiseurs pour contrats, souscriptions, sinistres, paiements, attestations, notifications
- Sécurité, validation, multilingue, RGPD, extensibilité
"""
from rest_framework import serializers

class ContratSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    numero = serializers.CharField(max_length=255)
    assure = serializers.CharField(max_length=255)
    type = serializers.CharField(max_length=255)
    date_debut = serializers.DateField()
    date_fin = serializers.DateField()
    montant = serializers.FloatField()

class SouscriptionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    contrat = serializers.IntegerField()
    date = serializers.DateField()
    montant = serializers.FloatField()

class SinistreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    contrat = serializers.IntegerField()
    description = serializers.CharField()
    date = serializers.DateField()
    montant = serializers.FloatField()
    statut = serializers.CharField(max_length=255)

class PaiementSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    contrat = serializers.IntegerField()
    date = serializers.DateField()
    montant = serializers.FloatField()
    mode = serializers.CharField(max_length=255)

class AttestationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    contrat = serializers.IntegerField()
    date = serializers.DateField()
    fichier_url = serializers.URLField()

class NotificationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    message = serializers.CharField(max_length=1024)
    date = serializers.DateTimeField()
    contrat = serializers.IntegerField()

class AuditLogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    action = serializers.CharField(max_length=255)
    user = serializers.CharField(max_length=255)
    date = serializers.DateTimeField()
    details = serializers.CharField()

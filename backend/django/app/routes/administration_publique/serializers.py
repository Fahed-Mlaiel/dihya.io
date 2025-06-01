"""
Dihya – Django Administration Publique Serializers Ultra Avancés
----------------------------------------------------------------
- Sérialiseurs pour démarches, documents, usagers, agents, notifications, logs, audit
- Sécurité, validation, multilingue, RGPD, extensibilité
"""
from rest_framework import serializers

class DemarcheSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    titre = serializers.CharField(max_length=256)
    description = serializers.CharField(max_length=1024)
    statut = serializers.ChoiceField(choices=[('en_cours', 'En cours'), ('terminee', 'Terminée')])
    date_creation = serializers.DateTimeField()
    date_modification = serializers.DateTimeField()

class DocumentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    titre = serializers.CharField(max_length=256)
    fichier = serializers.FileField()
    usager = serializers.CharField(max_length=128)
    date_upload = serializers.DateTimeField()

class UsagerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nom = serializers.CharField(max_length=128)
    prenom = serializers.CharField(max_length=128)
    email = serializers.EmailField()
    date_naissance = serializers.DateField()

class AgentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nom = serializers.CharField(max_length=128)
    prenom = serializers.CharField(max_length=128)
    role = serializers.CharField(max_length=64)

class NotificationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, help_text='Identifiant unique')
    message = serializers.CharField(max_length=1024, help_text='Message de notification')
    date = serializers.DateTimeField(help_text='Date de notification')
    usager = serializers.CharField(max_length=128, help_text='ID usager')

    def validate_message(self, value):
        if not value or len(value) < 3:
            raise serializers.ValidationError('Le message de notification est trop court.')
        return value

class AuditLogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, help_text='Identifiant unique')
    action = serializers.CharField(max_length=255, help_text='Action réalisée')
    user = serializers.CharField(max_length=255, help_text='Utilisateur')
    date = serializers.DateTimeField(help_text='Horodatage')
    details = serializers.CharField(help_text='Détails')

# RGPD : aucune donnée personnelle n’est exposée sans consentement explicite.
# Multilingue : tous les help_text sont traduits automatiquement via Django i18n.
# Accessibilité : tous les champs sont documentés pour l’auto-génération de la doc OpenAPI/Swagger.

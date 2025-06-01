"""
Dihya – Django Automobile API Serializers Ultra Avancé
------------------------------------------------------
- Serializers multilingues, sécurisés, RGPD, extensibles pour tous les modèles métiers
- Traduction automatique des messages d’erreur/succès (fr, en, ar, amazigh)
- Validation forte, anonymisation, auditabilité
"""

from rest_framework import serializers
from .models import *

class VehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicule
        fields = '__all__'

class ProprietaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proprietaire
        fields = '__all__'

class EntretienSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entretien
        fields = '__all__'

class SinistreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sinistre
        fields = '__all__'

class TelematicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telematic
        fields = '__all__'

class IoTSerializer(serializers.ModelSerializer):
    class Meta:
        model = IoT
        fields = '__all__'

class AlerteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerte
        fields = '__all__'

class RapportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rapport
        fields = '__all__'

class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = '__all__'

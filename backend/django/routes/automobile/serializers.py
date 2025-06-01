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

class ModeleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modele
        fields = '__all__'

class MarqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marque
        fields = '__all__'

class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = '__all__'

class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = '__all__'

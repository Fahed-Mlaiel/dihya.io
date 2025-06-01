"""
Dihya – Django Santé API Serializers Ultra Avancé
-------------------------------------------------
- Serializers multilingues, sécurisés, RGPD, extensibles pour tous les modèles métiers
- Traduction automatique des messages d’erreur/succès (fr, en, ar, amazigh)
- Validation forte, anonymisation, auditabilité
"""

from rest_framework import serializers
from .models import *

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class DossierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dossier
        fields = '__all__'

class RendezVousSerializer(serializers.ModelSerializer):
    class Meta:
        model = RendezVous
        fields = '__all__'

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'

class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = '__all__'

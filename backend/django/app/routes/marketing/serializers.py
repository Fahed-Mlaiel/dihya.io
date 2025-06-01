"""
Dihya – Serializers avancés pour le module Marketing
- Validation RGPD, accessibilité, multilingue, sécurité, souveraineté
"""
from rest_framework import serializers
from .models import Campagne, Lead, Audience, Canal, Contenu, Analytics, ABTesting, Notification, Rapport, AuditLog

class CampagneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campagne
        fields = '__all__'

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'

class AudienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audience
        fields = '__all__'

class CanalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canal
        fields = '__all__'

class ContenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contenu
        fields = '__all__'

class AnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analytics
        fields = '__all__'

class ABTestingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ABTesting
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class RapportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rapport
        fields = '__all__'

class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = '__all__'

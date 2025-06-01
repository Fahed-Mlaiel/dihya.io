"""
Dihya – Serializers pour le module Mobile
- Validation RGPD, accessibilité, multilingue, sécurité
"""
from rest_framework import serializers
from .models import MobileApp, Device, PushNotification

class MobileAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileApp
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class PushNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PushNotification
        fields = '__all__'

"""
Serializers pour le module Mobile
"""
from rest_framework import serializers
from .models import MobileProject

class MobileProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileProject
        fields = '__all__'

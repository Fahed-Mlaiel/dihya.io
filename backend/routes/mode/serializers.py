"""
Serializers pour le module Mode (Fashion)
"""
from rest_framework import serializers
from .models import ModeProject

class ModeProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeProject
        fields = '__all__'

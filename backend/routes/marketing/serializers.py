"""
Serializers pour le module Marketing
"""
from rest_framework import serializers
from .models import MarketingProject

class MarketingProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketingProject
        fields = '__all__'

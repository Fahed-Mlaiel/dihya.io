"""
Serializers pour le module Agriculture
"""
from rest_framework import serializers
from .models import AgricultureProject, AgricultureAsset

class AgricultureProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgricultureProject
        fields = '__all__'

class AgricultureAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgricultureAsset
        fields = '__all__'

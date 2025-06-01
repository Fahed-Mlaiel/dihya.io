"""
Serializers pour le module Industrie
"""
from rest_framework import serializers
from .models import IndustrieProject, IndustrieAsset

class IndustrieProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustrieProject
        fields = '__all__'

class IndustrieAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustrieAsset
        fields = '__all__'

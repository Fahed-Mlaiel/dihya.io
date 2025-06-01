"""
Serializers pour le module Medias
"""
from rest_framework import serializers
from .models import MediaAsset

class MediaAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaAsset
        fields = '__all__'

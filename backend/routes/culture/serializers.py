from rest_framework import serializers
from .models import CultureProject, CultureAsset
class CultureProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CultureProject
        fields = '__all__'
class CultureAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CultureAsset
        fields = '__all__'

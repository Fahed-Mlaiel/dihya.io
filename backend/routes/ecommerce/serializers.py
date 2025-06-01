from rest_framework import serializers
from .models import EcommerceProject, EcommerceAsset
class EcommerceProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcommerceProject
        fields = '__all__'
class EcommerceAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcommerceAsset
        fields = '__all__'

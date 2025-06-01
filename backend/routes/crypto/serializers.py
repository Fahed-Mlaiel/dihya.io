from rest_framework import serializers
from .models import CryptoProject, CryptoAsset
class CryptoProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoProject
        fields = '__all__'
class CryptoAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoAsset
        fields = '__all__'

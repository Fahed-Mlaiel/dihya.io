from rest_framework import serializers
from .models import BanqueFinanceProject, BanqueFinanceAsset
class BanqueFinanceProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = BanqueFinanceProject
        fields = '__all__'
class BanqueFinanceAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BanqueFinanceAsset
        fields = '__all__'

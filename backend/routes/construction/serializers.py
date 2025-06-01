from rest_framework import serializers
from .models import ConstructionProject, ConstructionAsset
class ConstructionProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstructionProject
        fields = '__all__'
class ConstructionAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstructionAsset
        fields = '__all__'

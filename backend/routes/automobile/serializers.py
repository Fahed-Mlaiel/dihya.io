from rest_framework import serializers
from .models import AutomobileProject, AutomobileAsset
class AutomobileProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutomobileProject
        fields = '__all__'
class AutomobileAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutomobileAsset
        fields = '__all__'

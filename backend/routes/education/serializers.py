from rest_framework import serializers
from .models import EducationProject, EducationAsset
class EducationProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationProject
        fields = '__all__'
class EducationAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationAsset
        fields = '__all__'

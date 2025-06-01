from rest_framework import serializers
from .models import BeauteProject, BeauteAsset
class BeauteProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeauteProject
        fields = '__all__'
class BeauteAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeauteAsset
        fields = '__all__'

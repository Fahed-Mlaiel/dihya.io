from rest_framework import serializers
from .models import BtpProject, BtpAsset
class BtpProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = BtpProject
        fields = '__all__'
class BtpAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BtpAsset
        fields = '__all__'

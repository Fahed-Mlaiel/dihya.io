"""
Serializers pour le module Administration Publique
"""
from rest_framework import serializers
from .models import AdministrationPubliqueProject

class AdministrationPubliqueProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdministrationPubliqueProject
        fields = '__all__'

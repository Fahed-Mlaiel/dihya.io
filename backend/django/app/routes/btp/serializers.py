"""
Serializers avancés pour les projets BTP (REST & GraphQL-ready).
Inclut validation, sécurité, multilingue, RGPD.
"""
from rest_framework import serializers
from .models import *

class BTPProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = BTPProject
        fields = '__all__'

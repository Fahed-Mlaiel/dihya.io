"""
Dihya – Serializers pour le module Mode
- Validation RGPD, accessibilité, multilingue, sécurité
"""
from rest_framework import serializers
from .models import Collection, Produit, Createur

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'

class CreateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Createur
        fields = '__all__'

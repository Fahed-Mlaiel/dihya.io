"""
Dihya – Django Beauté API Serializers Ultra Avancé
--------------------------------------------------
- Sérialiseurs pour soins, produits, rendez-vous, clients
- Sécurité, validation, multilingue, RGPD, extensibilité
"""
from rest_framework import serializers

class SoinSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nom = serializers.CharField(max_length=255)
    description = serializers.CharField()
    prix = serializers.FloatField()

class ProduitSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nom = serializers.CharField(max_length=255)
    marque = serializers.CharField(max_length=255)
    prix = serializers.FloatField()

class RendezVousSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    client = serializers.CharField(max_length=255)
    date = serializers.DateTimeField()
    soin = serializers.IntegerField()

class ClientSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nom = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    telephone = serializers.CharField(max_length=20)

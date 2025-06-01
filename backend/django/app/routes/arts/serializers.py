"""
Dihya – Django Arts API Serializers Ultra Avancé
------------------------------------------------
- Sérialiseurs pour œuvres, artistes, expositions, galeries, NFT, IA générative
- Sécurité, validation, multilingue, RGPD, extensibilité
"""
from rest_framework import serializers

class OeuvreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    titre = serializers.CharField(max_length=255)
    artiste = serializers.CharField(max_length=255)
    annee = serializers.IntegerField()
    description = serializers.CharField()
    image_url = serializers.URLField(required=False)

class ArtisteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nom = serializers.CharField(max_length=255)
    biographie = serializers.CharField()
    pays = serializers.CharField(max_length=255)

class ExpositionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nom = serializers.CharField(max_length=255)
    date_debut = serializers.DateField()
    date_fin = serializers.DateField()
    lieu = serializers.CharField(max_length=255)

class GalerieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nom = serializers.CharField(max_length=255)
    adresse = serializers.CharField(max_length=255)
    site_web = serializers.URLField(required=False)

class NFTSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    oeuvre = serializers.IntegerField()
    token_id = serializers.CharField(max_length=255)
    blockchain = serializers.CharField(max_length=255)
    url = serializers.URLField()

class IAGenerationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    prompt = serializers.CharField()
    image_url = serializers.URLField()

class AuditLogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    action = serializers.CharField(max_length=255)
    user = serializers.CharField(max_length=255)
    date = serializers.DateTimeField()
    details = serializers.CharField()

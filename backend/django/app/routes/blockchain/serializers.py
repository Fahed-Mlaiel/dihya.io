"""
Dihya – Django Blockchain API Serializers Ultra Avancé
------------------------------------------------------
- Sérialiseurs pour blocks, transactions, smart contracts, audit
- Sécurité, validation, multilingue, RGPD, extensibilité
"""
from rest_framework import serializers

class BlockSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    hash = serializers.CharField(max_length=255)
    previous_hash = serializers.CharField(max_length=255)
    timestamp = serializers.DateTimeField()
    nonce = serializers.IntegerField()

class TransactionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    block = serializers.IntegerField()
    sender = serializers.CharField(max_length=255)
    recipient = serializers.CharField(max_length=255)
    amount = serializers.FloatField()
    signature = serializers.CharField(max_length=512)
    timestamp = serializers.DateTimeField()

class SmartContractSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    code = serializers.CharField()
    owner = serializers.CharField(max_length=255)
    deployed_at = serializers.DateTimeField()

class AuditLogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    action = serializers.CharField(max_length=255)
    user = serializers.CharField(max_length=255)
    date = serializers.DateTimeField()
    details = serializers.CharField()

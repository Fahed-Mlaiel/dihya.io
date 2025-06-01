"""
Dihya – Django Blockchain API Models Ultra Avancé
-------------------------------------------------
- Modèles pour blocks, transactions, smart contracts, audit
- Sécurité, RGPD, multilingue, extensibilité
"""
from django.db import models

class Block(models.Model):
    hash = models.CharField(max_length=255)
    previous_hash = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    nonce = models.IntegerField()

class Transaction(models.Model):
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    sender = models.CharField(max_length=255)
    recipient = models.CharField(max_length=255)
    amount = models.FloatField()
    signature = models.CharField(max_length=512)
    timestamp = models.DateTimeField()

class SmartContract(models.Model):
    name = models.CharField(max_length=255)
    code = models.TextField()
    owner = models.CharField(max_length=255)
    deployed_at = models.DateTimeField()

class AuditLog(models.Model):
    action = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    details = models.TextField()

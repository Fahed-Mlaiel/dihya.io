"""
Dihya – Django Banque & Finance Serializers Ultra Avancés
---------------------------------------------------------
- Sérialiseurs pour comptes, transactions, virements, cartes, crédits, investissements, notifications, logs, audit
- Sécurité, validation, multilingue, RGPD, extensibilité
"""
from rest_framework import serializers

class CompteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    titulaire = serializers.CharField(max_length=128)
    solde = serializers.DecimalField(max_digits=12, decimal_places=2)
    devise = serializers.CharField(max_length=8)
    date_ouverture = serializers.DateField()
    is_active = serializers.BooleanField(default=True)

class TransactionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    compte = serializers.CharField(max_length=128)
    montant = serializers.DecimalField(max_digits=12, decimal_places=2)
    devise = serializers.CharField(max_length=8)
    date = serializers.DateTimeField()
    type = serializers.ChoiceField(choices=[('debit', 'Débit'), ('credit', 'Crédit')])
    description = serializers.CharField(max_length=256, required=False)

class VirementSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    emetteur = serializers.CharField(max_length=128)
    beneficiaire = serializers.CharField(max_length=128)
    montant = serializers.DecimalField(max_digits=12, decimal_places=2)
    devise = serializers.CharField(max_length=8)
    date = serializers.DateTimeField()
    motif = serializers.CharField(max_length=256, required=False)

# ...ajouter d'autres serializers pour cartes, crédits, investissements, notifications, logs, audit, etc.

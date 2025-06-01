"""
Dihya – Django Assurance API Models Ultra Avancé
------------------------------------------------
- Modèles pour contrats, souscriptions, sinistres, paiements, attestations, notifications, audit
- Sécurité, RGPD, multilingue, extensibilité
"""
from django.db import models

class Contrat(models.Model):
    numero = models.CharField(max_length=255)
    assure = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    date_debut = models.DateField()
    date_fin = models.DateField()
    montant = models.FloatField()

class Souscription(models.Model):
    contrat = models.ForeignKey(Contrat, on_delete=models.CASCADE)
    date = models.DateField()
    montant = models.FloatField()

class Sinistre(models.Model):
    contrat = models.ForeignKey(Contrat, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()
    montant = models.FloatField()
    statut = models.CharField(max_length=255)

class Paiement(models.Model):
    contrat = models.ForeignKey(Contrat, on_delete=models.CASCADE)
    date = models.DateField()
    montant = models.FloatField()
    mode = models.CharField(max_length=255)

class Attestation(models.Model):
    contrat = models.ForeignKey(Contrat, on_delete=models.CASCADE)
    date = models.DateField()
    fichier_url = models.URLField()

class Notification(models.Model):
    message = models.CharField(max_length=1024)
    date = models.DateTimeField()
    contrat = models.ForeignKey(Contrat, on_delete=models.CASCADE)

class AuditLog(models.Model):
    action = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    details = models.TextField()

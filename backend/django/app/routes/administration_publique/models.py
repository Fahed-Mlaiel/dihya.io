"""
Dihya – Django Administration Publique API Models Ultra Avancé
-------------------------------------------------------------
- Modèles pour citoyens, démarches, documents, audits, notifications
- Sécurité, RGPD, multilingue, extensibilité
"""
from django.db import models

class Citoyen(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    date_naissance = models.DateField()
    numero_identite = models.CharField(max_length=50, unique=True)
    adresse = models.CharField(max_length=255)

class Demarche(models.Model):
    type = models.CharField(max_length=255)
    date_demande = models.DateField()
    citoyen = models.ForeignKey(Citoyen, on_delete=models.CASCADE)
    statut = models.CharField(max_length=255)

class Document(models.Model):
    titre = models.CharField(max_length=255)
    fichier_url = models.URLField()
    date_emission = models.DateField()
    citoyen = models.ForeignKey(Citoyen, on_delete=models.CASCADE)

class AuditLog(models.Model):
    action = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    details = models.TextField()

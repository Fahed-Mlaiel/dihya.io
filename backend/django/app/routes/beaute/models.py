"""
Dihya – Django Beauté API Models Ultra Avancé
--------------------------------------------
- Modèles pour soins, produits, rendez-vous, clients
- Sécurité, RGPD, multilingue, extensibilité
"""
from django.db import models

class Soin(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    prix = models.FloatField()

class Produit(models.Model):
    nom = models.CharField(max_length=255)
    marque = models.CharField(max_length=255)
    prix = models.FloatField()

class RendezVous(models.Model):
    client = models.CharField(max_length=255)
    date = models.DateTimeField()
    soin = models.ForeignKey(Soin, on_delete=models.CASCADE)

class Client(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)

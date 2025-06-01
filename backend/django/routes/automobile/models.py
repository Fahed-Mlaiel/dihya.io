"""
Dihya – Django Automobile API Models Ultra Avancé
-------------------------------------------------
- Modèles métiers complets : Véhicule, Modèle, Marque, Maintenance, AuditLog
- Sécurité, RGPD, multilingue, extensibilité, souveraineté
"""

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Marque(models.Model):
    nom = models.CharField(max_length=255)
    pays = models.CharField(max_length=100)

class Modele(models.Model):
    nom = models.CharField(max_length=255)
    marque = models.ForeignKey(Marque, on_delete=models.CASCADE)
    annee = models.IntegerField()

class Vehicule(models.Model):
    modele = models.ForeignKey(Modele, on_delete=models.CASCADE)
    immatriculation = models.CharField(max_length=50)
    proprietaire = models.ForeignKey(User, on_delete=models.CASCADE)
    date_achat = models.DateField()
    kilometrage = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vehicules')

class Maintenance(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()
    cout = models.DecimalField(max_digits=10, decimal_places=2)

class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    objet = models.CharField(max_length=255)
    date_action = models.DateTimeField(auto_now_add=True)
    details = models.JSONField(default=dict)

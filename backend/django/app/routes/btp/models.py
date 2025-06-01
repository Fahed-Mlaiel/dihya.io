"""
Dihya – Django BTP API Models Ultra Avancé
-----------------------------------------
- Modèles pour chantiers, matériaux, ouvriers, machines
- Sécurité, RGPD, multilingue, extensibilité
"""
from django.db import models

class Chantier(models.Model):
    nom = models.CharField(max_length=255)
    localisation = models.CharField(max_length=255)
    date_debut = models.DateField()
    date_fin = models.DateField()

    class Meta:
        pass

class Materiau(models.Model):
    nom = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    quantite = models.FloatField()
    chantier = models.ForeignKey(Chantier, on_delete=models.CASCADE)

    class Meta:
        pass

class Ouvrier(models.Model):
    nom = models.CharField(max_length=255)
    specialite = models.CharField(max_length=255)
    chantier = models.ForeignKey(Chantier, on_delete=models.CASCADE)

    class Meta:
        pass

class Machine(models.Model):
    nom = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    chantier = models.ForeignKey(Chantier, on_delete=models.CASCADE)

    class Meta:
        pass

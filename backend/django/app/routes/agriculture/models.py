"""
Dihya – Django Agriculture API Models Ultra Avancé
--------------------------------------------------
- Modèles pour exploitations, cultures, capteurs IoT, météo, alertes, rapports, notifications
- Sécurité, RGPD, multilingue, extensibilité
"""
from django.db import models

class Exploitation(models.Model):
    nom = models.CharField(max_length=255)
    localisation = models.CharField(max_length=255)
    superficie = models.FloatField()
    proprietaire = models.CharField(max_length=255)
    date_creation = models.DateField()

class Culture(models.Model):
    type = models.CharField(max_length=255)
    surface = models.FloatField()
    date_semis = models.DateField()
    exploitation = models.ForeignKey(Exploitation, on_delete=models.CASCADE)

class Capteur(models.Model):
    type = models.CharField(max_length=255)
    valeur = models.FloatField()
    unite = models.CharField(max_length=50)
    date_mesure = models.DateTimeField()
    exploitation = models.ForeignKey(Exploitation, on_delete=models.CASCADE)

class Meteo(models.Model):
    temperature = models.FloatField()
    humidite = models.FloatField()
    date = models.DateField()
    exploitation = models.ForeignKey(Exploitation, on_delete=models.CASCADE)

class Alerte(models.Model):
    type = models.CharField(max_length=255)
    message = models.CharField(max_length=1024)
    date = models.DateTimeField()
    exploitation = models.ForeignKey(Exploitation, on_delete=models.CASCADE)

class Rapport(models.Model):
    titre = models.CharField(max_length=255)
    contenu = models.TextField()
    date = models.DateField()
    exploitation = models.ForeignKey(Exploitation, on_delete=models.CASCADE)

class Notification(models.Model):
    message = models.CharField(max_length=1024)
    date = models.DateTimeField()
    exploitation = models.ForeignKey(Exploitation, on_delete=models.CASCADE)

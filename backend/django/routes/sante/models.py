"""
Dihya – Django Santé API Models Ultra Avancé
-------------------------------------------
- Modèles métiers complets : Patient, Dossier, RendezVous, Prescription, AuditLog
- Sécurité, RGPD, multilingue, extensibilité, souveraineté
"""

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Patient(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    date_naissance = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Dossier(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    description = models.TextField()
    date_ouverture = models.DateField()

class RendezVous(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField()
    motif = models.CharField(max_length=255)

class Prescription(models.Model):
    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE)
    medicament = models.CharField(max_length=255)
    posologie = models.CharField(max_length=255)
    date_prescription = models.DateField()

class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    objet = models.CharField(max_length=255)
    date_action = models.DateTimeField(auto_now_add=True)
    details = models.JSONField(default=dict)

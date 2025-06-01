"""
Dihya – Modèles Django pour le module Santé
- Gestion des patients, rendez-vous, dossiers médicaux, RGPD, sécurité
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class Patient(models.Model):
    nom = models.CharField(max_length=255, help_text=_('Nom du patient'))
    prenom = models.CharField(max_length=255, help_text=_('Prénom du patient'))
    date_naissance = models.DateField(help_text=_('Date de naissance'))
    email = models.EmailField(help_text=_('Email du patient'))
    telephone = models.CharField(max_length=20, help_text=_('Téléphone'))
    genre = models.CharField(max_length=20, choices=[('homme', _('Homme')), ('femme', _('Femme')), ('autre', _('Autre'))], help_text=_('Genre'))
    class Meta:
        verbose_name = _('Patient')
        verbose_name_plural = _('Patients')
    def __str__(self):
        return f"{self.prenom} {self.nom}"

class RendezVous(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='rendezvous', help_text=_('Patient concerné'))
    date = models.DateTimeField(help_text=_('Date du rendez-vous'))
    motif = models.CharField(max_length=255, help_text=_('Motif du rendez-vous'))
    statut = models.CharField(max_length=50, choices=[('planifie', _('Planifié')), ('termine', _('Terminé')), ('annule', _('Annulé'))], default='planifie', help_text=_('Statut du rendez-vous'))
    class Meta:
        verbose_name = _('Rendez-vous')
        verbose_name_plural = _('Rendez-vous')
    def __str__(self):
        return f"{self.patient} - {self.date}"

class DossierMedical(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='dossiers', help_text=_('Patient concerné'))
    description = models.TextField(help_text=_('Description du dossier'))
    date_ouverture = models.DateField(help_text=_('Date d’ouverture'))
    actif = models.BooleanField(default=True, help_text=_('Dossier actif'))
    class Meta:
        verbose_name = _('Dossier médical')
        verbose_name_plural = _('Dossiers médicaux')
    def __str__(self):
        return f"{self.patient} - {self.date_ouverture}"

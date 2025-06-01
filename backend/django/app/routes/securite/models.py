"""
Dihya – Modèles Django pour le module Sécurité
- Gestion des incidents, alertes, contrôles, RGPD, sécurité
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class IncidentSecurite(models.Model):
    titre = models.CharField(max_length=255, help_text=_('Titre de l’incident'))
    description = models.TextField(help_text=_('Description de l’incident'))
    date_signalement = models.DateTimeField(auto_now_add=True)
    niveau = models.CharField(max_length=50, choices=[('mineur', _('Mineur')), ('majeur', _('Majeur')), ('critique', _('Critique'))], help_text=_('Niveau de gravité'))
    signale_par = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, help_text=_('Utilisateur ayant signalé'))
    resolu = models.BooleanField(default=False, help_text=_('Incident résolu'))
    class Meta:
        verbose_name = _('Incident de sécurité')
        verbose_name_plural = _('Incidents de sécurité')
    def __str__(self):
        return self.titre

class AlerteSecurite(models.Model):
    titre = models.CharField(max_length=255, help_text=_('Titre de l’alerte'))
    message = models.TextField(help_text=_('Message d’alerte'))
    date_emission = models.DateTimeField(auto_now_add=True)
    niveau = models.CharField(max_length=50, choices=[('info', _('Info')), ('avertissement', _('Avertissement')), ('critique', _('Critique'))], help_text=_('Niveau d’alerte'))
    actif = models.BooleanField(default=True, help_text=_('Alerte active'))
    class Meta:
        verbose_name = _('Alerte de sécurité')
        verbose_name_plural = _('Alertes de sécurité')
    def __str__(self):
        return self.titre

class ControleSecurite(models.Model):
    nom = models.CharField(max_length=255, help_text=_('Nom du contrôle'))
    description = models.TextField(help_text=_('Description du contrôle'))
    date_controle = models.DateField(help_text=_('Date du contrôle'))
    conforme = models.BooleanField(default=True, help_text=_('Contrôle conforme'))
    class Meta:
        verbose_name = _('Contrôle de sécurité')
        verbose_name_plural = _('Contrôles de sécurité')
    def __str__(self):
        return self.nom

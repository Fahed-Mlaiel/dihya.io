"""
Dihya – Modèles Django pour le module Publicité
- Gestion des campagnes publicitaires, canaux, analytics, RGPD, sécurité
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class CampagnePublicitaire(models.Model):
    nom = models.CharField(max_length=255, help_text=_('Nom de la campagne publicitaire'))
    canal = models.CharField(max_length=100, help_text=_('Canal utilisé (display, social, search, etc.)'))
    budget = models.DecimalField(max_digits=12, decimal_places=2, help_text=_('Budget alloué'))
    date_debut = models.DateTimeField(help_text=_('Date de début'))
    date_fin = models.DateTimeField(help_text=_('Date de fin'))
    statut = models.CharField(max_length=50, choices=[('brouillon', _('Brouillon')), ('active', _('Active')), ('terminee', _('Terminée'))], default='brouillon', help_text=_('Statut de la campagne'))
    cree_par = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, help_text=_('Créateur'))
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = _('Campagne publicitaire')
        verbose_name_plural = _('Campagnes publicitaires')
        app_label = 'publicite'
    def __str__(self):
        return self.nom

class AnalyticsPublicite(models.Model):
    campagne = models.ForeignKey(CampagnePublicitaire, on_delete=models.CASCADE, related_name='analytics', help_text=_('Campagne associée'))
    impressions = models.PositiveIntegerField(default=0, help_text=_('Nombre d’impressions'))
    clics = models.PositiveIntegerField(default=0, help_text=_('Nombre de clics'))
    conversions = models.PositiveIntegerField(default=0, help_text=_('Nombre de conversions'))
    date = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = _('Analytics publicité')
        verbose_name_plural = _('Analytics publicités')
        app_label = 'publicite'
    def __str__(self):
        return f"Analytics {self.campagne.nom} - {self.date}"

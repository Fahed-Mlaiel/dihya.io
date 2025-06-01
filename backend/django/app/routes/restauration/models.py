"""
Dihya – Modèles Django pour le module Restauration
- Gestion des restaurants, menus, réservations, RGPD, sécurité
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class Restaurant(models.Model):
    nom = models.CharField(max_length=255, help_text=_('Nom du restaurant'))
    adresse = models.CharField(max_length=255, help_text=_('Adresse'))
    telephone = models.CharField(max_length=20, help_text=_('Téléphone'))
    proprietaire = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, help_text=_('Propriétaire'))
    actif = models.BooleanField(default=True, help_text=_('Restaurant actif'))
    class Meta:
        verbose_name = _('Restaurant')
        verbose_name_plural = _('Restaurants')
        app_label = 'restauration'
    def __str__(self):
        return self.nom

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus', help_text=_('Restaurant associé'))
    nom = models.CharField(max_length=255, help_text=_('Nom du menu'))
    description = models.TextField(blank=True, help_text=_('Description du menu'))
    prix = models.DecimalField(max_digits=8, decimal_places=2, help_text=_('Prix'))
    disponible = models.BooleanField(default=True, help_text=_('Menu disponible'))
    class Meta:
        verbose_name = _('Menu')
        verbose_name_plural = _('Menus')
        app_label = 'restauration'
    def __str__(self):
        return self.nom

class Reservation(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reservations', help_text=_('Restaurant associé'))
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, help_text=_('Client'))
    date = models.DateTimeField(help_text=_('Date de la réservation'))
    nombre_personnes = models.PositiveIntegerField(help_text=_('Nombre de personnes'))
    statut = models.CharField(max_length=50, choices=[('en_attente', _('En attente')), ('confirmee', _('Confirmée')), ('annulee', _('Annulée'))], default='en_attente', help_text=_('Statut de la réservation'))
    class Meta:
        verbose_name = _('Réservation')
        verbose_name_plural = _('Réservations')
        app_label = 'restauration'
    def __str__(self):
        return f"{self.restaurant} - {self.date}"

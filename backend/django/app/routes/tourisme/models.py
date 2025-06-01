"""
Dihya – Modèles Django pour le module Tourisme
- Gestion des offres, destinations, réservations, avis, guides, événements, partenaires, RGPD, sécurité
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

class Destination(models.Model):
    nom = models.CharField(max_length=255, help_text=_('Nom de la destination'))
    pays = models.CharField(max_length=100, help_text=_('Pays'))
    description = models.TextField(help_text=_('Description'))
    class Meta:
        verbose_name = _('Destination')
        verbose_name_plural = _('Destinations')
    def __str__(self):
        return self.nom

class Offre(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='offres', help_text=_('Destination'))
    titre = models.CharField(max_length=255, help_text=_('Titre de l’offre'))
    description = models.TextField(help_text=_('Description de l’offre'))
    prix = models.DecimalField(max_digits=10, decimal_places=2, help_text=_('Prix'))
    date_debut = models.DateField(help_text=_('Date de début'))
    date_fin = models.DateField(help_text=_('Date de fin'))
    class Meta:
        verbose_name = _('Offre')
        verbose_name_plural = _('Offres')
    def __str__(self):
        return self.titre

class Reservation(models.Model):
    offre = models.ForeignKey(Offre, on_delete=models.CASCADE, related_name='reservations', help_text=_('Offre'))
    nom_client = models.CharField(max_length=255, help_text=_('Nom du client'))
    email_client = models.EmailField(help_text=_('Email du client'))
    date_reservation = models.DateField(help_text=_('Date de réservation'))
    statut = models.CharField(max_length=50, choices=[('en_attente', _('En attente')), ('confirmee', _('Confirmée')), ('annulee', _('Annulée'))], default='en_attente', help_text=_('Statut de la réservation'))
    class Meta:
        verbose_name = _('Réservation')
        verbose_name_plural = _('Réservations')
    def __str__(self):
        return f"{self.nom_client} - {self.offre}"

class Avis(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='avis', help_text=_('Réservation'))
    note = models.IntegerField(help_text=_('Note (1-5)'))
    commentaire = models.TextField(help_text=_('Commentaire'))
    date_avis = models.DateField(help_text=_('Date de l’avis'))
    class Meta:
        verbose_name = _('Avis')
        verbose_name_plural = _('Avis')
    def __str__(self):
        return f"Avis {self.note}/5 - {self.reservation}"

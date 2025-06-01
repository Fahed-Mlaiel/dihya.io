"""
Dihya – Modèles Django pour le module Services à la Personne
- Gestion des prestations, bénéficiaires, intervenants, RGPD, sécurité
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class Beneficiaire(models.Model):
    nom = models.CharField(max_length=255, help_text=_('Nom du bénéficiaire'))
    prenom = models.CharField(max_length=255, help_text=_('Prénom du bénéficiaire'))
    email = models.EmailField(help_text=_('Email du bénéficiaire'))
    telephone = models.CharField(max_length=20, help_text=_('Téléphone'))
    adresse = models.CharField(max_length=255, help_text=_('Adresse'))
    class Meta:
        verbose_name = _('Bénéficiaire')
        verbose_name_plural = _('Bénéficiaires')
    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Intervenant(models.Model):
    nom = models.CharField(max_length=255, help_text=_('Nom de l’intervenant'))
    prenom = models.CharField(max_length=255, help_text=_('Prénom de l’intervenant'))
    email = models.EmailField(help_text=_('Email de l’intervenant'))
    specialite = models.CharField(max_length=100, help_text=_('Spécialité'))
    class Meta:
        verbose_name = _('Intervenant')
        verbose_name_plural = _('Intervenants')
    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Prestation(models.Model):
    beneficiaire = models.ForeignKey(Beneficiaire, on_delete=models.CASCADE, related_name='prestations', help_text=_('Bénéficiaire'))
    intervenant = models.ForeignKey(Intervenant, on_delete=models.SET_NULL, null=True, help_text=_('Intervenant'))
    type_prestation = models.CharField(max_length=100, help_text=_('Type de prestation'))
    date = models.DateTimeField(help_text=_('Date de la prestation'))
    statut = models.CharField(max_length=50, choices=[('planifiee', _('Planifiée')), ('effectuee', _('Effectuée')), ('annulee', _('Annulée'))], default='planifiee', help_text=_('Statut de la prestation'))
    class Meta:
        verbose_name = _('Prestation')
        verbose_name_plural = _('Prestations')
    def __str__(self):
        return f"{self.type_prestation} - {self.date}"

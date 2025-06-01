"""
Dihya – Modèles Django pour le module Ressources Humaines
- Gestion des employés, postes, candidatures, RGPD, sécurité
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class Employe(models.Model):
    nom = models.CharField(max_length=255, help_text=_('Nom de l’employé'))
    prenom = models.CharField(max_length=255, help_text=_('Prénom de l’employé'))
    email = models.EmailField(help_text=_('Email professionnel'))
    poste = models.CharField(max_length=100, help_text=_('Poste occupé'))
    date_embauche = models.DateField(help_text=_('Date d’embauche'))
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, help_text=_('Manager'))
    actif = models.BooleanField(default=True, help_text=_('Employé actif'))
    class Meta:
        verbose_name = _('Employé')
        verbose_name_plural = _('Employés')
        app_label = 'ressources_humaines'
    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Poste(models.Model):
    titre = models.CharField(max_length=255, help_text=_('Titre du poste'))
    description = models.TextField(blank=True, help_text=_('Description du poste'))
    ouvert = models.BooleanField(default=True, help_text=_('Poste ouvert au recrutement'))
    class Meta:
        verbose_name = _('Poste')
        verbose_name_plural = _('Postes')
        app_label = 'ressources_humaines'
    def __str__(self):
        return self.titre

class Candidature(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE, related_name='candidatures', help_text=_('Employé concerné'))
    poste = models.ForeignKey(Poste, on_delete=models.CASCADE, related_name='candidatures', help_text=_('Poste visé'))
    date_candidature = models.DateField(auto_now_add=True)
    statut = models.CharField(max_length=50, choices=[('en_attente', _('En attente')), ('acceptee', _('Acceptée')), ('refusee', _('Refusée'))], default='en_attente', help_text=_('Statut de la candidature'))
    class Meta:
        verbose_name = _('Candidature')
        verbose_name_plural = _('Candidatures')
        app_label = 'ressources_humaines'
    def __str__(self):
        return f"{self.employe} - {self.poste}"

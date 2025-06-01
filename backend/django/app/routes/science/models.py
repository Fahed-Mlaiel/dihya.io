"""
Dihya – Modèles Django pour le module Science
- Gestion des projets scientifiques, publications, chercheurs, RGPD, sécurité
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class ProjetScientifique(models.Model):
    titre = models.CharField(max_length=255, help_text=_('Titre du projet'))
    description = models.TextField(help_text=_('Description du projet'))
    date_debut = models.DateField(help_text=_('Date de début'))
    date_fin = models.DateField(help_text=_('Date de fin'))
    responsable = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, help_text=_('Responsable du projet'))
    class Meta:
        verbose_name = _('Projet scientifique')
        verbose_name_plural = _('Projets scientifiques')
    def __str__(self):
        return self.titre

class Publication(models.Model):
    projet = models.ForeignKey(ProjetScientifique, on_delete=models.CASCADE, related_name='publications', help_text=_('Projet associé'))
    titre = models.CharField(max_length=255, help_text=_('Titre de la publication'))
    date_publication = models.DateField(help_text=_('Date de publication'))
    resume = models.TextField(blank=True, help_text=_('Résumé'))
    class Meta:
        verbose_name = _('Publication')
        verbose_name_plural = _('Publications')
    def __str__(self):
        return self.titre

class Chercheur(models.Model):
    nom = models.CharField(max_length=255, help_text=_('Nom du chercheur'))
    prenom = models.CharField(max_length=255, help_text=_('Prénom du chercheur'))
    email = models.EmailField(help_text=_('Email du chercheur'))
    specialite = models.CharField(max_length=100, help_text=_('Spécialité'))
    projets = models.ManyToManyField(ProjetScientifique, related_name='chercheurs', blank=True, help_text=_('Projets associés'))
    class Meta:
        verbose_name = _('Chercheur')
        verbose_name_plural = _('Chercheurs')
    def __str__(self):
        return f"{self.prenom} {self.nom}"

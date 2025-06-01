"""
Dihya – Modèles Django pour le module Recherche
- Gestion des requêtes, index, résultats, RGPD, sécurité
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class RequeteRecherche(models.Model):
    terme = models.CharField(max_length=255, help_text=_('Terme recherché'))
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, help_text=_('Utilisateur'))
    date_recherche = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = _('Requête de recherche')
        verbose_name_plural = _('Requêtes de recherche')
        app_label = 'recherche'
    def __str__(self):
        return self.terme

class ResultatRecherche(models.Model):
    requete = models.ForeignKey(RequeteRecherche, on_delete=models.CASCADE, related_name='resultats', help_text=_('Requête associée'))
    titre = models.CharField(max_length=255, help_text=_('Titre du résultat'))
    url = models.URLField(help_text=_('URL du résultat'))
    extrait = models.TextField(blank=True, help_text=_('Extrait'))
    score = models.FloatField(default=0, help_text=_('Score de pertinence'))
    class Meta:
        verbose_name = _('Résultat de recherche')
        verbose_name_plural = _('Résultats de recherche')
        app_label = 'recherche'
    def __str__(self):
        return self.titre

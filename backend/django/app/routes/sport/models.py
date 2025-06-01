"""
Dihya – Modèles Django pour le module Sport
- Gestion des clubs, équipes, athlètes, compétitions, résultats, entraînements, billetterie, RGPD, sécurité
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

class Club(models.Model):
    nom = models.CharField(max_length=255, help_text=_('Nom du club'))
    ville = models.CharField(max_length=100, help_text=_('Ville'))
    date_fondation = models.DateField(help_text=_('Date de fondation'))
    class Meta:
        verbose_name = _('Club')
        verbose_name_plural = _('Clubs')
    def __str__(self):
        return self.nom

class Equipe(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='equipes', help_text=_('Club'))
    nom = models.CharField(max_length=255, help_text=_('Nom de l’équipe'))
    categorie = models.CharField(max_length=100, help_text=_('Catégorie'))
    class Meta:
        verbose_name = _('Équipe')
        verbose_name_plural = _('Équipes')
    def __str__(self):
        return self.nom

class Athlete(models.Model):
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE, related_name='athletes', help_text=_('Équipe'))
    nom = models.CharField(max_length=255, help_text=_('Nom de l’athlète'))
    prenom = models.CharField(max_length=255, help_text=_('Prénom de l’athlète'))
    date_naissance = models.DateField(help_text=_('Date de naissance'))
    class Meta:
        verbose_name = _('Athlète')
        verbose_name_plural = _('Athlètes')
    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Competition(models.Model):
    nom = models.CharField(max_length=255, help_text=_('Nom de la compétition'))
    date = models.DateField(help_text=_('Date de la compétition'))
    lieu = models.CharField(max_length=255, help_text=_('Lieu'))
    class Meta:
        verbose_name = _('Compétition')
        verbose_name_plural = _('Compétitions')
    def __str__(self):
        return self.nom

class Resultat(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, related_name='resultats', help_text=_('Compétition'))
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE, related_name='resultats', help_text=_('Équipe'))
    score = models.CharField(max_length=50, help_text=_('Score'))
    classement = models.IntegerField(help_text=_('Classement'))
    class Meta:
        verbose_name = _('Résultat')
        verbose_name_plural = _('Résultats')
    def __str__(self):
        return f"{self.equipe} - {self.competition} : {self.score}"

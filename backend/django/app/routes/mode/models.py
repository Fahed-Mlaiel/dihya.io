"""
Dihya – Modèles Django pour le module Mode
- Gestion des collections, produits, créateurs, tendances, RGPD, sécurité
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class Collection(models.Model):
    nom = models.CharField(max_length=255, help_text=_('Nom de la collection'))
    saison = models.CharField(max_length=50, help_text=_('Saison (printemps, été, automne, hiver)'))
    annee = models.PositiveIntegerField(help_text=_('Année'))
    description = models.TextField(blank=True, help_text=_('Description'))
    cree_par = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, help_text=_('Créateur'))
    class Meta:
        verbose_name = _('Collection')
        verbose_name_plural = _('Collections')
    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=255, help_text=_('Nom du produit'))
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='produits', help_text=_('Collection associée'))
    prix = models.DecimalField(max_digits=10, decimal_places=2, help_text=_('Prix'))
    taille = models.CharField(max_length=20, help_text=_('Taille'))
    couleur = models.CharField(max_length=50, help_text=_('Couleur'))
    description = models.TextField(blank=True, help_text=_('Description'))
    disponible = models.BooleanField(default=True, help_text=_('Disponible'))
    class Meta:
        verbose_name = _('Produit')
        verbose_name_plural = _('Produits')
    def __str__(self):
        return self.nom

class Createur(models.Model):
    nom = models.CharField(max_length=255, help_text=_('Nom du créateur'))
    bio = models.TextField(blank=True, help_text=_('Biographie'))
    pays = models.CharField(max_length=100, help_text=_('Pays'))
    class Meta:
        verbose_name = _('Créateur')
        verbose_name_plural = _('Créateurs')
    def __str__(self):
        return self.nom

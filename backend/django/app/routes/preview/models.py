"""
Dihya – Modèles Django pour le module Preview
- Gestion des aperçus de contenus, sécurité, RGPD, accessibilité
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class Preview(models.Model):
    titre = models.CharField(max_length=255, help_text=_('Titre de l’aperçu'))
    contenu = models.TextField(help_text=_('Contenu à prévisualiser'))
    type = models.CharField(max_length=50, help_text=_('Type de contenu (texte, image, vidéo, etc.)'))
    date_creation = models.DateTimeField(auto_now_add=True)
    cree_par = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, help_text=_('Créateur'))
    class Meta:
        verbose_name = _('Aperçu')
        verbose_name_plural = _('Aperçus')
        app_label = 'preview'
    def __str__(self):
        return self.titre

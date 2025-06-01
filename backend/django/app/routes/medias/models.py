"""
Dihya – Modèles Django pour le module Médias
- Gestion des médias, contenus, métadonnées, accessibilité, RGPD, sécurité
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class Media(models.Model):
    titre = models.CharField(max_length=255, help_text=_('Titre du média / Media title'))
    description = models.TextField(blank=True, help_text=_('Description du média'))
    fichier = models.FileField(upload_to='medias/', help_text=_('Fichier média'))
    type = models.CharField(max_length=50, choices=[('image', _('Image')), ('video', _('Vidéo')), ('audio', _('Audio')), ('document', _('Document'))], help_text=_('Type de média'))
    date_upload = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, help_text=_('Utilisateur'))
    is_public = models.BooleanField(default=False, help_text=_('Média public'))
    class Meta:
        verbose_name = _('Média')
        verbose_name_plural = _('Médias')
        app_label = 'medias'
    def __str__(self):
        return self.titre

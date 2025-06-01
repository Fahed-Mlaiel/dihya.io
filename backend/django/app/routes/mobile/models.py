"""
Dihya – Modèles Django pour le module Mobile
- Gestion des applications mobiles, devices, notifications push, RGPD, sécurité
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class MobileApp(models.Model):
    nom = models.CharField(max_length=255, help_text=_('Nom de l’application mobile'))
    plateforme = models.CharField(max_length=50, choices=[('android', _('Android')), ('ios', _('iOS'))], help_text=_('Plateforme'))
    version = models.CharField(max_length=20, help_text=_('Version de l’application'))
    date_publication = models.DateTimeField(help_text=_('Date de publication'))
    description = models.TextField(blank=True, help_text=_('Description'))
    cree_par = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, help_text=_('Créateur'))
    class Meta:
        verbose_name = _('Application mobile')
        verbose_name_plural = _('Applications mobiles')
        app_label = 'mobile'
    def __str__(self):
        return self.nom

class Device(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, help_text=_('Utilisateur'))
    device_id = models.CharField(max_length=255, help_text=_('ID du device'))
    plateforme = models.CharField(max_length=50, choices=[('android', _('Android')), ('ios', _('iOS'))], help_text=_('Plateforme'))
    date_enregistrement = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = _('Device')
        verbose_name_plural = _('Devices')
        app_label = 'mobile'
    def __str__(self):
        return f"{self.user} - {self.device_id}"

class PushNotification(models.Model):
    titre = models.CharField(max_length=255, help_text=_('Titre de la notification'))
    message = models.TextField(help_text=_('Message'))
    device = models.ForeignKey(Device, on_delete=models.CASCADE, help_text=_('Device cible'))
    date_envoi = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=50, choices=[('envoyee', _('Envoyée')), ('echouee', _('Échouée'))], default='envoyee', help_text=_('Statut'))
    class Meta:
        verbose_name = _('Notification push')
        verbose_name_plural = _('Notifications push')
        app_label = 'mobile'
    def __str__(self):
        return self.titre

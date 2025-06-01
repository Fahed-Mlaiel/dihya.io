"""
Dihya – Modèles utilitaires pour API Utils
- Pour la gestion des logs, conversions, monitoring, etc.
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

class LogEntry(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, help_text=_('Horodatage'))
    niveau = models.CharField(max_length=50, help_text=_('Niveau'))
    message = models.TextField(help_text=_('Message'))
    utilisateur = models.CharField(max_length=255, blank=True, help_text=_('Utilisateur'))
    class Meta:
        verbose_name = _('Entrée de log')
        verbose_name_plural = _('Entrées de log')
        app_label = 'utils'
    def __str__(self):
        return f"[{self.timestamp}] {self.niveau}: {self.message[:50]}"

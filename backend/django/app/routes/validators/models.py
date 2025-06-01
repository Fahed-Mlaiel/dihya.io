"""
Dihya – Modèles pour Validators
- Pour la gestion des validations, logs, schémas, etc.
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

class ValidationLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, help_text=_('Horodatage'))
    type_validation = models.CharField(max_length=100, help_text=_('Type de validation'))
    resultat = models.CharField(max_length=50, help_text=_('Résultat'))
    details = models.TextField(help_text=_('Détails'))
    utilisateur = models.CharField(max_length=255, blank=True, help_text=_('Utilisateur'))
    class Meta:
        verbose_name = _('Log de validation')
        verbose_name_plural = _('Logs de validation')
        app_label = 'validators'
    def __str__(self):
        return f"[{self.timestamp}] {self.type_validation}: {self.resultat}"

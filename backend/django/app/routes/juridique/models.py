"""
Modèles Juridique (exemple ultra avancé, multilingue, RGPD, accessibilité)
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

class DossierJuridique(models.Model):
    titre = models.CharField(max_length=255, help_text=_('Titre du dossier / Case title / عنوان الملف / ⵜⴰⵙⵉⵏⵜ ⵏ ⴰⴷ┰ⵙ'))
    description = models.TextField(help_text=_('Description / الوصف / ⵜⴰⵙⵉⵏⵜ'))
    type = models.CharField(max_length=100, help_text=_('Type (contrat, litige, etc.) / Type / النوع / ⵜⴰⵙⵉⵏⵜ'))
    responsable = models.CharField(max_length=255, help_text=_('Responsable / Manager / المسؤول / ⴰⵎⴰⵣⵉⵖ'))
    date_creation = models.DateTimeField(auto_now_add=True, help_text=_('Date de création / Creation date / تاريخ الإنشاء / ⴰⵙⴳⴰⵙ ⵏ ⴰⴷⵔⴰⵙ'))
    # RGPD: pas de données personnelles sensibles
    class Meta:
        verbose_name = _('Dossier juridique')
        verbose_name_plural = _('Dossiers juridiques')
        app_label = 'juridique'

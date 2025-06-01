"""
Modèles Environnement (exemple ultra avancé, multilingue, RGPD, accessibilité)
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

class SiteEnvironnement(models.Model):
    nom = models.CharField(max_length=255, help_text=_('Nom du site / Site name / اسم الموقع / ⵉⵙⴰⵏ ⵏ ⵜⴰⵙⵉⵏⵜ'))
    type = models.CharField(max_length=100, help_text=_('Type (forêt, zone humide, réserve, etc.) / Type / النوع / ⵜⴰⵙⵉⵏⵜ'))
    superficie = models.DecimalField(max_digits=12, decimal_places=2, help_text=_('Superficie (ha) / Area / المساحة / ⵜⴰⵙⵉⵏⵜ'))
    localisation = models.CharField(max_length=255, help_text=_('Localisation / Location / الموقع / ⵜⴰⵏⴰⴷⵜ'))
    responsable = models.CharField(max_length=255, help_text=_('Responsable / Manager / المسؤول / ⴰⵎⴰⵣⵉⵖ'))
    date_creation = models.DateTimeField(auto_now_add=True, help_text=_('Date de création / Creation date / تاريخ الإنشاء / ⴰⵙⴳⴰⵙ ⵏ ⵜⴰⵙⵉⵏⵜ'))
    # RGPD: pas de données personnelles sensibles
    class Meta:
        verbose_name = _('Site environnemental')
        verbose_name_plural = _('Sites environnementaux')

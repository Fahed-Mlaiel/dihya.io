"""
Modèles Construction (exemple ultra avancé, multilingue, RGPD, accessibilité)
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

class Chantier(models.Model):
    nom = models.CharField(max_length=255, help_text=_('Nom du chantier / Site name / اسم الورشة / ⵉⵙⴰⵏ ⵏ ⵛⴰⵏⵜⵉⵔ'))
    localisation = models.CharField(max_length=255, help_text=_('Localisation / Location / الموقع / ⵜⴰⵏⴰⴷⵜ'))
    date_debut = models.DateField(help_text=_('Date de début / Start date / تاريخ البداية / ⴰⵙⴳⴰⵙ ⵏ ⵜⴰⵏⵜⵉⵔ'))
    date_fin = models.DateField(help_text=_('Date de fin / End date / تاريخ النهاية / ⴰⵙⴳⴰⵙ ⵏ ⵜⴰⵏⵜⵉⵔ'))
    responsable = models.CharField(max_length=255, help_text=_('Responsable / Manager / المسؤول / ⴰⵎⴰⵣⵉⵖ'))
    budget = models.DecimalField(max_digits=12, decimal_places=2, help_text=_('Budget (€) / الميزانية / ⴱⵓⴳⴰⵜ'))
    # RGPD: pas de données personnelles sensibles
    class Meta:
        verbose_name = _('Chantier')
        verbose_name_plural = _('Chantiers')

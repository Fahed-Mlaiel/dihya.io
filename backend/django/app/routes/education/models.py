"""
Modèles Éducation (exemple ultra avancé, multilingue, RGPD, accessibilité)
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

class Etablissement(models.Model):
    nom = models.CharField(max_length=255, help_text=_('Nom de l’établissement / School name / اسم المؤسسة / ⵉⵙⴰⵏ ⵏ ⵜⴰⵙⵉⵏⵜ'))
    adresse = models.CharField(max_length=255, help_text=_('Adresse / Address / العنوان / ⵜⴰⵏⴰⴷⵜ'))
    responsable = models.CharField(max_length=255, help_text=_('Responsable / Manager / المسؤول / ⴰⵎⴰⵣⵉⵖ'))
    date_creation = models.DateTimeField(auto_now_add=True, help_text=_('Date de création / Creation date / تاريخ الإنشاء / ⴰⵙⴳⴰⵙ ⵏ ⵜⴰⵙⵉⵏⵜ'))
    # RGPD: pas de données personnelles sensibles
    class Meta:
        verbose_name = _('Établissement')
        verbose_name_plural = _('Établissements')

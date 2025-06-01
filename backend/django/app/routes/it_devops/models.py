"""
Modèles IT & DevOps (exemple ultra avancé, multilingue, RGPD, accessibilité)
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

class Pipeline(models.Model):
    nom = models.CharField(max_length=255, help_text=_('Nom du pipeline / Pipeline name / اسم خط الأنابيب / ⵉⵙⴰⵏ ⵏ pipeline'))
    type = models.CharField(max_length=100, help_text=_('Type (CI, CD, monitoring, etc.) / Type / النوع / ⵜⴰⵙⵉⵏⵜ'))
    status = models.CharField(max_length=50, help_text=_('Statut / Status / الحالة / ⵜⴰⵙⵉⵏⵜ'))
    responsable = models.CharField(max_length=255, help_text=_('Responsable / Manager / المسؤول / ⴰⵎⴰⵣⵉⵖ'))
    date_creation = models.DateTimeField(auto_now_add=True, help_text=_('Date de création / Creation date / تاريخ الإنشاء / ⴰⵙⴳⴰⵙ ⵏ pipeline'))
    # RGPD: pas de données personnelles sensibles
    class Meta:
        verbose_name = _('Pipeline')
        verbose_name_plural = _('Pipelines')

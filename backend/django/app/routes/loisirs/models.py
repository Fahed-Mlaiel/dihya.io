"""
Modèles Loisirs (exemple ultra avancé, multilingue, RGPD, accessibilité)
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

class ActiviteLoisir(models.Model):
    nom = models.CharField(max_length=255, help_text=_('Nom de l’activité / Activity name / اسم النشاط / ⵉⵙⴰⵏ ⵏ ⵜⴰⵙⵉⵏⵜ'))
    type = models.CharField(max_length=100, help_text=_('Type (sport, club, événement, etc.) / Type / النوع / ⵜⴰⵙⵉⵏⵜ'))
    lieu = models.CharField(max_length=255, help_text=_('Lieu / Location / المكان / ⵜⴰⵏⴰⴷⵜ'))
    responsable = models.CharField(max_length=255, help_text=_('Responsable / Manager / المسؤول / ⴰⵎⴰⵣⵉⵖ'))
    date_creation = models.DateTimeField(auto_now_add=True, help_text=_('Date de création / Creation date / تاريخ الإنشاء / ⴰⵙⴳⴰⵙ ⵏ ⵜⴰⵙⵉⵏⵜ'))
    # RGPD: pas de données personnelles sensibles
    class Meta:
        verbose_name = _('Activité loisir')
        verbose_name_plural = _('Activités loisirs')
        app_label = 'loisirs'

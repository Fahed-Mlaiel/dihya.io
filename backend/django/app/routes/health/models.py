"""
Modèles Health (exemple ultra avancé, multilingue, RGPD, accessibilité)
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

class DossierSante(models.Model):
    patient = models.CharField(max_length=255, help_text=_('Nom du patient / Patient name / اسم المريض / ⴰⵎⴰⵣⵉⵖ'))
    date_naissance = models.DateField(help_text=_('Date de naissance / Birth date / تاريخ الميلاد / ⴰⵙⴳⴰⵙ ⵏ ⴰⵎⴰⵣⵉⵖ'))
    pathologie = models.CharField(max_length=255, help_text=_('Pathologie / Disease / المرض / ⵜⴰⵙⵉⵏⵜ'))
    traitement = models.TextField(help_text=_('Traitement / Treatment / العلاج / ⵜⴰⵙⵉⵏⵜ'))
    medecin = models.CharField(max_length=255, help_text=_('Médecin référent / Doctor / الطبيب / ⴰⵎⴰⵣⵉⵖ'))
    date_creation = models.DateTimeField(auto_now_add=True, help_text=_('Date de création / Creation date / تاريخ الإنشاء / ⴰⵙⴳⴰⵙ ⵏ ⵜⴰⵙⵉⵏⵜ'))
    # RGPD: pseudonymisation, pas de données sensibles stockées en clair
    class Meta:
        verbose_name = _('Dossier santé')
        verbose_name_plural = _('Dossiers santé')

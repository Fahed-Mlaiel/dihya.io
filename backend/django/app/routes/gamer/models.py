"""
Modèles Gamer (exemple ultra avancé, multilingue, RGPD, accessibilité)
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

class ProfilGamer(models.Model):
    pseudo = models.CharField(max_length=255, help_text=_('Pseudonyme / Username / اسم المستخدم / ⴰⵎⴰⵣⵉⵖ'))
    score = models.IntegerField(help_text=_('Score / النقاط / ⴰⴳⴷⴰⴷ'))
    niveau = models.CharField(max_length=100, help_text=_('Niveau / Level / المستوى / ⵜⴰⵙⵉⵏⵜ'))
    date_inscription = models.DateTimeField(auto_now_add=True, help_text=_('Date d’inscription / Registration date / تاريخ التسجيل / ⴰⵙⴳⴰⵙ ⵏ ⵜⴰⵙⵉⵏⵜ'))
    # RGPD: pas de données personnelles sensibles
    class Meta:
        verbose_name = _('Profil gamer')
        verbose_name_plural = _('Profils gamers')

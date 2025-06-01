"""
Modèles Culture (exemple ultra avancé, multilingue, RGPD, accessibilité)
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

class EvenementCulturel(models.Model):
    titre = models.CharField(max_length=255, help_text=_('Titre de l’événement / Event title / عنوان الحدث / ⵜⴰⵙⵉⵏⵜ ⵏ ⴰⵙⵉⵏⵜ'))
    description = models.TextField(help_text=_('Description / الوصف / ⵜⴰⵙⵉⵏⵜ'))
    date = models.DateField(help_text=_('Date / التاريخ / ⴰⵙⴳⴰⵙ'))
    lieu = models.CharField(max_length=255, help_text=_('Lieu / Location / المكان / ⵜⴰⵏⴰⴷⵜ'))
    organisateur = models.CharField(max_length=255, help_text=_('Organisateur / Organizer / المنظم / ⴰⵎⴰⵣⵉⵖ'))
    # RGPD: pas de données personnelles sensibles
    class Meta:
        verbose_name = _('Événement culturel')
        verbose_name_plural = _('Événements culturels')

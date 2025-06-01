"""
Modèles Immobilier (exemple ultra avancé, multilingue, RGPD, accessibilité)
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

class BienImmobilier(models.Model):
    titre = models.CharField(max_length=255, help_text=_('Titre du bien / Asset title / عنوان العقار / ⵜⴰⵙⵉⵏⵜ ⵏ ⴱⵉⵏ'))
    description = models.TextField(help_text=_('Description / الوصف / ⵜⴰⵙⵉⵏⵜ'))
    type = models.CharField(max_length=100, help_text=_('Type (appartement, maison, terrain, etc.) / Type / النوع / ⵜⴰⵙⵉⵏⵜ'))
    surface = models.DecimalField(max_digits=10, decimal_places=2, help_text=_('Surface (m²) / Area / المساحة / ⵜⴰⵙⵉⵏⵜ'))
    localisation = models.CharField(max_length=255, help_text=_('Localisation / Location / الموقع / ⵜⴰⵏⴰⴷⵜ'))
    prix = models.DecimalField(max_digits=12, decimal_places=2, help_text=_('Prix (€) / Price / السعر / ⴰⴳⴷⴰⴷ'))
    proprietaire = models.CharField(max_length=255, help_text=_('Propriétaire / Owner / المالك / ⴰⵎⴰⵣⵉⵖ'))
    date_creation = models.DateTimeField(auto_now_add=True, help_text=_('Date de création / Creation date / تاريخ الإنشاء / ⴰⵙⴳⴰⵙ ⵏ ⴱⵉⵏ'))
    # RGPD: pas de données personnelles sensibles
    class Meta:
        verbose_name = _('Bien immobilier')
        verbose_name_plural = _('Biens immobiliers')

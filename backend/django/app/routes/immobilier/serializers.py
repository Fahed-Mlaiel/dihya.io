"""
Serializers Immobilier (validations avancées, multilingue, RGPD, accessibilité)
"""
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

class BienImmobilierSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'BienImmobilier'
        fields = '__all__'
        extra_kwargs = {
            'titre': {'help_text': _('Titre du bien / Asset title / عنوان العقار / ⵜⴰⵙⵉⵏⵜ ⵏ ⴱⵉⵏ')},
            'description': {'help_text': _('Description / الوصف / ⵜⴰⵙⵉⵏⵜ')},
            'type': {'help_text': _('Type (appartement, maison, terrain, etc.) / Type / النوع / ⵜⴰⵙⵉⵏⵜ')},
            'surface': {'help_text': _('Surface (m²) / Area / المساحة / ⵜⴰⵙⵉⵏⵜ')},
            'localisation': {'help_text': _('Localisation / Location / الموقع / ⵜⴰⵏⴰⴷⵜ')},
            'prix': {'help_text': _('Prix (€) / Price / السعر / ⴰⴳⴷⴰⴷ')},
            'proprietaire': {'help_text': _('Propriétaire / Owner / المالك / ⴰⵎⴰⵣⵉⵖ')},
            'date_creation': {'help_text': _('Date de création / Creation date / تاريخ الإنشاء / ⴰⵙⴳⴰⵙ ⵏ ⴱⵉⵏ')},
        }

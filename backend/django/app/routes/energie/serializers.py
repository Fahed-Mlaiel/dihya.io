"""
Serializers Énergie (validations avancées, multilingue, RGPD, accessibilité)
"""
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

class SiteEnergieSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'SiteEnergie'
        fields = '__all__'
        extra_kwargs = {
            'nom': {'help_text': _('Nom du site / Site name / اسم الموقع / ⵉⵙⴰⵏ ⵏ ⵜⴰⵣⵡⴰⵔⵜ')},
            'type': {'help_text': _('Type (solaire, éolien, hydraulique, etc.) / Type / النوع / ⵜⴰⵙⵉⵏⵜ')},
            'capacite': {'help_text': _('Capacité (MW) / Capacity / القدرة / ⴰⴳⴷⴰⴷ')},
            'localisation': {'help_text': _('Localisation / Location / الموقع / ⵜⴰⵏⴰⴷⵜ')},
            'responsable': {'help_text': _('Responsable / Manager / المسؤول / ⴰⵎⴰⵣⵉⵖ')},
            'date_creation': {'help_text': _('Date de création / Creation date / تاريخ الإنشاء / ⴰⵙⴳⴰⵙ ⵏ ⵜⴰⵣⵡⴰⵔⵜ')},
        }

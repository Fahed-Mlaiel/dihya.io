"""
Serializers Environnement (validations avancées, multilingue, RGPD, accessibilité)
"""
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

class SiteEnvironnementSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'SiteEnvironnement'
        fields = '__all__'
        extra_kwargs = {
            'nom': {'help_text': _('Nom du site / Site name / اسم الموقع / ⵉⵙⴰⵏ ⵏ ⵜⴰⵙⵉⵏⵜ')},
            'type': {'help_text': _('Type (forêt, zone humide, réserve, etc.) / Type / النوع / ⵜⴰⵙⵉⵏⵜ')},
            'superficie': {'help_text': _('Superficie (ha) / Area / المساحة / ⵜⴰⵙⵉⵏⵜ')},
            'localisation': {'help_text': _('Localisation / Location / الموقع / ⵜⴰⵏⴰⴷⵜ')},
            'responsable': {'help_text': _('Responsable / Manager / المسؤول / ⴰⵎⴰⵣⵉⵖ')},
            'date_creation': {'help_text': _('Date de création / Creation date / تاريخ الإنشاء / ⴰⵙⴳⴰⵙ ⵏ ⵜⴰⵙⵉⵏⵜ')},
        }

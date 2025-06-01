"""
Serializers Hôtellerie (validations avancées, multilingue, RGPD, accessibilité)
"""
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'Hotel'
        fields = '__all__'
        extra_kwargs = {
            'nom': {'help_text': _('Nom de l’hôtel / Hotel name / اسم الفندق / ⵉⵙⴰⵏ ⵏ ⵉⵀⵓⵜⴰⵍ')},
            'adresse': {'help_text': _('Adresse / Address / العنوان / ⵜⴰⵏⴰⴷⵜ')},
            'responsable': {'help_text': _('Responsable / Manager / المسؤول / ⴰⵎⴰⵣⵉⵖ')},
            'date_creation': {'help_text': _('Date de création / Creation date / تاريخ الإنشاء / ⴰⵙⴳⴰⵙ ⵏ ⵉⵀⵓⵜⴰⵍ')},
        }

"""
Serializers Éducation (validations avancées, multilingue, RGPD, accessibilité)
"""
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

class EtablissementSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'Etablissement'
        fields = '__all__'
        extra_kwargs = {
            'nom': {'help_text': _('Nom de l’établissement / School name / اسم المؤسسة / ⵉⵙⴰⵏ ⵏ ⵜⴰⵙⵉⵏⵜ')},
            'adresse': {'help_text': _('Adresse / Address / العنوان / ⵜⴰⵏⴰⴷⵜ')},
            'responsable': {'help_text': _('Responsable / Manager / المسؤول / ⴰⵎⴰⵣⵉⵖ')},
            'date_creation': {'help_text': _('Date de création / Creation date / تاريخ الإنشاء / ⴰⵙⴳⴰⵙ ⵏ ⵜⴰⵙⵉⵏⵜ')},
        }

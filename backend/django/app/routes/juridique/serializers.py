"""
Serializers Juridique (validations avancées, multilingue, RGPD, accessibilité)
"""
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

class DossierJuridiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'DossierJuridique'
        fields = '__all__'
        extra_kwargs = {
            'titre': {'help_text': _('Titre du dossier / Case title / عنوان الملف / ⵜⴰⵙⵉⵏⵜ ⵏ ⴰⴷⵔⴰⵙ')},
            'description': {'help_text': _('Description / الوصف / ⵜⴰⵙⵉⵏⵜ')},
            'type': {'help_text': _('Type (contrat, litige, etc.) / Type / النوع / ⵜⴰⵙⵉⵏⵜ')},
            'responsable': {'help_text': _('Responsable / Manager / المسؤول / ⴰⵎⴰⵣⵉⵖ')},
            'date_creation': {'help_text': _('Date de création / Creation date / تاريخ الإنشاء / ⴰⵙⴳⴰⵙ ⵏ ⴰⴷⵔⴰⵙ')},
        }

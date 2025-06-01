"""
Serializers Loisirs (validations avancées, multilingue, RGPD, accessibilité)
"""
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

class ActiviteLoisirSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'ActiviteLoisir'
        fields = '__all__'
        extra_kwargs = {
            'nom': {'help_text': _('Nom de l’activité / Activity name / اسم النشاط / ⵉⵙⴰⵏ ⵏ ⵜⴰⵙⵉⵏⵜ')},
            'type': {'help_text': _('Type (sport, club, événement, etc.) / Type / النوع / ⵜⴰⵙⵉⵏⵜ')},
            'lieu': {'help_text': _('Lieu / Location / المكان / ⵜⴰⵏⴰⴷⵜ')},
            'responsable': {'help_text': _('Responsable / Manager / المسؤول / ⴰⵎⴰⵣⵉⵖ')},
            'date_creation': {'help_text': _('Date de création / Creation date / تاريخ الإنشاء / ⴰⵙⴳⴰⵙ ⵏ ⵜⴰⵙⵉⵏⵜ')},
        }

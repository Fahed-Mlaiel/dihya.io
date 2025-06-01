"""
Serializers Construction (validations avancées, multilingue, RGPD, accessibilité)
"""
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

class ChantierSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'Chantier'
        fields = '__all__'
        extra_kwargs = {
            'nom': {'help_text': _('Nom du chantier / Site name / اسم الورشة / ⵉⵙⴰⵏ ⵏ ⵛⴰⵏⵜⵉⵔ')},
            'localisation': {'help_text': _('Localisation / Location / الموقع / ⵜⴰⵏⴰⴷⵜ')},
            'date_debut': {'help_text': _('Date de début / Start date / تاريخ البداية / ⴰⵙⴳⴰⵙ ⵏ ⵜⴰⵏⵜⵉⵔ')},
            'date_fin': {'help_text': _('Date de fin / End date / تاريخ النهاية / ⴰⵙⴳⴰⵙ ⵏ ⵜⴰⵏⵜⵉⵔ')},
            'responsable': {'help_text': _('Responsable / Manager / المسؤول / ⴰⵎⴰⵣⵉⵖ')},
            'budget': {'help_text': _('Budget (€) / الميزانية / ⴱⵓⴳⴰⵜ')},
        }

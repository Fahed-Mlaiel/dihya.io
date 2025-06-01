"""
Serializers IT & DevOps (validations avancées, multilingue, RGPD, accessibilité)
"""
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

class PipelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'Pipeline'
        fields = '__all__'
        extra_kwargs = {
            'nom': {'help_text': _('Nom du pipeline / Pipeline name / اسم خط الأنابيب / ⵉⵙⴰⵏ ⵏ pipeline')},
            'type': {'help_text': _('Type (CI, CD, monitoring, etc.) / Type / النوع / ⵜⴰⵙⵉⵏⵜ')},
            'status': {'help_text': _('Statut / Status / الحالة / ⵜⴰⵙⵉⵏⵜ')},
            'responsable': {'help_text': _('Responsable / Manager / المسؤول / ⴰⵎⴰⵣⵉⵖ')},
            'date_creation': {'help_text': _('Date de création / Creation date / تاريخ الإنشاء / ⴰⵙⴳⴰⵙ ⵏ pipeline')},
        }

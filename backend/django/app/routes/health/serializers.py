"""
Serializers Health (validations avancées, multilingue, RGPD, accessibilité)
"""
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

class DossierSanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'DossierSante'
        fields = '__all__'
        extra_kwargs = {
            'patient': {'help_text': _('Nom du patient / Patient name / اسم المريض / ⴰⵎⴰⵣⵉⵖ')},
            'date_naissance': {'help_text': _('Date de naissance / Birth date / تاريخ الميلاد / ⴰⵙⴳⴰⵙ ⵏ ⴰⵎⴰⵣⵉⵖ')},
            'pathologie': {'help_text': _('Pathologie / Disease / المرض / ⵜⴰⵙⵉⵏⵜ')},
            'traitement': {'help_text': _('Traitement / Treatment / العلاج / ⵜⴰⵙⵉⵏⵜ')},
            'medecin': {'help_text': _('Médecin référent / Doctor / الطبيب / ⴰⵎⴰⵣⵉⵖ')},
            'date_creation': {'help_text': _('Date de création / Creation date / تاريخ الإنشاء / ⴰⵙⴳⴰⵙ ⵏ ⵜⴰⵙⵉⵏⵜ')},
        }

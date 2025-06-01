"""
Serializers Gamer (validations avancées, multilingue, RGPD, accessibilité)
"""
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

class ProfilGamerSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'ProfilGamer'
        fields = '__all__'
        extra_kwargs = {
            'pseudo': {'help_text': _('Pseudonyme / Username / اسم المستخدم / ⴰⵎⴰⵣⵉⵖ')},
            'score': {'help_text': _('Score / النقاط / ⴰⴳⴷⴰⴷ')},
            'niveau': {'help_text': _('Niveau / Level / المستوى / ⵜⴰⵙⵉⵏⵜ')},
            'date_inscription': {'help_text': _('Date d’inscription / Registration date / تاريخ التسجيل / ⴰⵙⴳⴰⵙ ⵏ ⵜⴰⵙⵉⵏⵜ')},
        }

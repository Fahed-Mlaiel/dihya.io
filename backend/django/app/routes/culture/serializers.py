"""
Serializers Culture (validations avancées, multilingue, RGPD, accessibilité)
"""
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

class EvenementCulturelSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'EvenementCulturel'
        fields = '__all__'
        extra_kwargs = {
            'titre': {'help_text': _('Titre de l’événement / Event title / عنوان الحدث / ⵜⴰⵙⵉⵏⵜ ⵏ ⴰⵙⵉⵏⵜ')},
            'description': {'help_text': _('Description / الوصف / ⵜⴰⵙⵉⵏⵜ')},
            'date': {'help_text': _('Date / التاريخ / ⴰⵙⴳⴰⵙ')},
            'lieu': {'help_text': _('Lieu / Location / المكان / ⵜⴰⵏⴰⴷⵜ')},
            'organisateur': {'help_text': _('Organisateur / Organizer / المنظم / ⴰⵎⴰⵣⵉⵖ')},
        }

"""
Serializers Journalisme (validations avancées, multilingue, RGPD, accessibilité)
"""
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'Article'
        fields = '__all__'
        extra_kwargs = {
            'titre': {'help_text': _('Titre de l’article / Article title / عنوان المقال / ⵜⴰⵙⵉⵏⵜ ⵏ ⴰⵙⵉⵏⵜ')},
            'contenu': {'help_text': _('Contenu / Content / المحتوى / ⵜⴰⵙⵉⵏⵜ')},
            'auteur': {'help_text': _('Auteur / Author / الكاتب / ⴰⵎⴰⵣⵉⵖ')},
            'date_publication': {'help_text': _('Date de publication / Publication date / تاريخ النشر / ⴰⵙⴳⴰⵙ ⵏ ⵜⴰⵙⵉⵏⵜ')},
        }

"""
Modèles Journalisme (exemple ultra avancé, multilingue, RGPD, accessibilité)
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

class Article(models.Model):
    titre = models.CharField(max_length=255, help_text=_('Titre de l’article / Article title / عنوان المقال / ⵜⴰⵙⵉⵏⵜ ⵏ ⴰⵙⵉⵏⵜ'))
    contenu = models.TextField(help_text=_('Contenu / Content / المحتوى / ⵜⴰⵙⵉⵏⵜ'))
    auteur = models.CharField(max_length=255, help_text=_('Auteur / Author / الكاتب / ⴰⵎⴰⵣⵉⵖ'))
    date_publication = models.DateTimeField(help_text=_('Date de publication / Publication date / تاريخ النشر / ⴰⵙⴳⴰⵙ ⵏ ⵜⴰⵙⵉⵏⵜ'))
    # RGPD: pas de données personnelles sensibles
    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

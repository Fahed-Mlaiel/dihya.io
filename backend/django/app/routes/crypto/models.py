"""
Modèles Crypto (exemple ultra avancé, multilingue, RGPD, accessibilité)
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

class CryptoWallet(models.Model):
    adresse = models.CharField(max_length=255, help_text=_('Adresse du wallet / Wallet address / عنوان المحفظة / ⴰⴷ┰ⵙ ⵏ wallet'))
    solde = models.DecimalField(max_digits=20, decimal_places=8, help_text=_('Solde / Balance / الرصيد / ⴰⴳⴷⴰⴷ'))
    devise = models.CharField(max_length=10, help_text=_('Devise (BTC, ETH, etc.) / العملة / ⴰⴳⴷⴰⴷ'))
    proprietaire = models.CharField(max_length=255, help_text=_('Propriétaire (pseudonyme) / Owner / المالك / ⴰⵎⴰⵣⵉⵖ'))
    date_creation = models.DateTimeField(auto_now_add=True, help_text=_('Date de création / Creation date / تاريخ الإنشاء / ⴰⵙⴳⴰⵙ ⵏ ⴰⴷⵔⴰⵙ'))
    # RGPD: pas de données personnelles sensibles
    class Meta:
        verbose_name = _('Wallet crypto')
        verbose_name_plural = _('Wallets crypto')

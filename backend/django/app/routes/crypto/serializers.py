"""
Serializers Crypto (validations avancées, multilingue, RGPD, accessibilité)
"""
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

class CryptoWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'CryptoWallet'
        fields = '__all__'
        extra_kwargs = {
            'adresse': {'help_text': _('Adresse du wallet / Wallet address / عنوان المحفظة / ⴰⴷⵔⴰⵙ ⵏ wallet')},
            'solde': {'help_text': _('Solde / Balance / الرصيد / ⴰⴳⴷⴰⴷ')},
            'devise': {'help_text': _('Devise (BTC, ETH, etc.) / العملة / ⴰⴳⴷⴰⴷ')},
            'proprietaire': {'help_text': _('Propriétaire (pseudonyme) / Owner / المالك / ⴰⵎⴰⵣⵉⵖ')},
            'date_creation': {'help_text': _('Date de création / Creation date / تاريخ الإنشاء / ⴰⵙⴳⴰⵙ ⵏ ⴰⴷⵔⴰⵙ')},
        }

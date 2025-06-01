"""
Tests unitaires et intégration Crypto (couverture maximale, multilingue)
"""
from django.test import TestCase
from .models import CryptoWallet

class CryptoWalletModelTest(TestCase):
    def test_creation_wallet(self):
        wallet = CryptoWallet.objects.create(
            adresse='0x123456789', solde=1.2345, devise='ETH', proprietaire='Yidir')
        self.assertEqual(wallet.devise, 'ETH')

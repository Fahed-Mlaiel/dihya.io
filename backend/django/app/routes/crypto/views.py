"""
Views Crypto (API ultra avancée, sécurité, accessibilité, multilingue)
"""
from rest_framework import viewsets
from .models import CryptoWallet
from .serializers import CryptoWalletSerializer
from .permissions import IsWalletOwner

class CryptoWalletViewSet(viewsets.ModelViewSet):
    queryset = CryptoWallet.objects.all()
    serializer_class = CryptoWalletSerializer
    permission_classes = [IsWalletOwner]

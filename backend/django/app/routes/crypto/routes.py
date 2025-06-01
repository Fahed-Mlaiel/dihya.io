"""
Dihya – Django Crypto API Routes Ultra Avancé
---------------------------------------------
- Endpoints REST pour wallets, transactions, exchanges, cotations, NFT, tokens, staking, logs, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, multilingue, extensibilité
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST crypto (sécurité, multilingue, souveraineté)
🇬🇧 Django REST crypto routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للعملات الرقمية (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n crypto (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'wallets', views.WalletViewSet, basename='wallet')
router.register(r'transactions', views.TransactionViewSet, basename='transaction')
router.register(r'exchanges', views.ExchangeViewSet, basename='exchange')
router.register(r'tokens', views.TokenViewSet, basename='token')
router.register(r'nft', views.NFTViewSet, basename='nft')
router.register(r'staking', views.StakingViewSet, basename='staking')
router.register(r'cotations', views.CotationViewSet, basename='cotation')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Extensible : ajoutez vos endpoints (analyse IA, multi-blockchain, open data, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

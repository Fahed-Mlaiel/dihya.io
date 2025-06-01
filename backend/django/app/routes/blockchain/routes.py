"""
Dihya – Django Blockchain API Routes Ultra Avancé
-------------------------------------------------
- Endpoints REST pour blocks, transactions, smart contracts, audit
- Sécurité, RBAC, logs, conformité RGPD/NIS2, multilingue, extensibilité
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST blockchain (sécurité, multilingue, souveraineté)
🇬🇧 Django REST blockchain routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للبلوكشين (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n blockchain (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'blocks', views.BlockViewSet, basename='block')
router.register(r'transactions', views.TransactionViewSet, basename='transaction')
router.register(r'smartcontracts', views.SmartContractViewSet, basename='smartcontract')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Extensible : ajoutez vos endpoints (analyse IA, multi-blockchain, open data, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

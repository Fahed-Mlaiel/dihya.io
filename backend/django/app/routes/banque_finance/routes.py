"""
Dihya – Django Banque & Finance API Routes Ultra Avancé
-------------------------------------------------------
- Endpoints REST pour comptes, transactions, virements, cartes, crédits, investissements, notifications, logs, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, multilingue, extensibilité
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST banque & finance (sécurité, multilingue, souveraineté)
🇬🇧 Django REST banking & finance routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للبنوك والمالية (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n banque & finance (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'comptes', views.CompteViewSet, basename='compte')
router.register(r'transactions', views.TransactionViewSet, basename='transaction')
router.register(r'virements', views.VirementViewSet, basename='virement')
router.register(r'cartes', views.CarteViewSet, basename='carte')
router.register(r'credits', views.CreditViewSet, basename='credit')
router.register(r'investissements', views.InvestissementViewSet, basename='investissement')
router.register(r'releves', views.ReleveViewSet, basename='releve')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Extensible : ajoutez vos endpoints (scoring IA, open banking, open data, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

"""
Dihya – Django Immobilier API Routes Ultra Avancé
-------------------------------------------------
- Endpoints REST pour biens, transactions, locations, ventes, agences, mandats, visites, évaluations, IA, logs, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, multilingue, extensibilité
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST immobilier (sécurité, multilingue, souveraineté)
🇬🇧 Django REST real estate routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للعقارات (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n imiknawen (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'biens', views.BienViewSet, basename='bien')
router.register(r'transactions', views.TransactionViewSet, basename='transaction')
router.register(r'locations', views.LocationViewSet, basename='location')
router.register(r'ventes', views.VenteViewSet, basename='vente')
router.register(r'agences', views.AgenceViewSet, basename='agence')
router.register(r'mandats', views.MandatViewSet, basename='mandat')
router.register(r'visites', views.VisiteViewSet, basename='visite')
router.register(r'evaluations', views.EvaluationViewSet, basename='evaluation')
router.register(r'ia', views.IAImmobilierViewSet, basename='ia-immobilier')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

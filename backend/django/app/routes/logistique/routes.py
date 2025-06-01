"""
Dihya – Django Logistique API Routes Ultra Avancé
-------------------------------------------------
- Endpoints REST pour entrepôts, stocks, livraisons, expéditions, transporteurs, commandes, itinéraires, IA optimisation, logs, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, multilingue, extensibilité
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST logistique (sécurité, multilingue, souveraineté)
🇬🇧 Django REST logistics routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للوجستيات (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n tazrawt (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'entrepots', views.EntrepotViewSet, basename='entrepot')
router.register(r'stocks', views.StockViewSet, basename='stock')
router.register(r'livraisons', views.LivraisonViewSet, basename='livraison')
router.register(r'expeditions', views.ExpeditionViewSet, basename='expedition')
router.register(r'transporteurs', views.TransporteurViewSet, basename='transporteur')
router.register(r'commandes', views.CommandeViewSet, basename='commande')
router.register(r'itineraires', views.ItineraireViewSet, basename='itineraire')
router.register(r'suivi', views.SuiviColisViewSet, basename='suivi-colis')
router.register(r'ia', views.IALogistiqueViewSet, basename='ia-logistique')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

"""
Dihya – Django Restauration API Routes Ultra Avancé
---------------------------------------------------
- Endpoints REST pour restaurants, menus, plats, commandes, réservations, stocks, fournisseurs, avis, IA restauration, notifications, rapports, logs, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, anonymisation, multilingue, extensibilité, fallback IA open source
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST restauration (sécurité, multilingue, souveraineté)
🇬🇧 Django REST foodservice routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للمطاعم (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n tikkelt (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet, basename='restaurant')
router.register(r'menus', views.MenuViewSet, basename='menu')
router.register(r'plats', views.PlatViewSet, basename='plat')
router.register(r'commandes', views.CommandeViewSet, basename='commande')
router.register(r'reservations', views.ReservationViewSet, basename='reservation')
router.register(r'stocks', views.StockViewSet, basename='stock')
router.register(r'fournisseurs', views.FournisseurViewSet, basename='fournisseur')
router.register(r'avis', views.AvisViewSet, basename='avis')
router.register(r'ia', views.IARestaurationViewSet, basename='ia-restauration')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'rapports', views.RapportViewSet, basename='rapport')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, anonymisation, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Fallback IA open source : tous les endpoints critiques disposent d’un fallback open source
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

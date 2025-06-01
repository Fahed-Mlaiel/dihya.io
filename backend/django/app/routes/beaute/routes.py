"""
Dihya – Django Beauté API Routes Ultra Avancé
---------------------------------------------
- Endpoints REST pour salons, prestations, produits, réservations, avis, IA recommandation, logs, audit
- Sécurité, RBAC, logs, conformité RGPD/NIS2, multilingue, extensibilité
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST beauté (sécurité, multilingue, souveraineté)
🇬🇧 Django REST beauty routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للجمال (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n umalu (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'salons', views.SalonViewSet, basename='salon')
router.register(r'prestations', views.PrestationViewSet, basename='prestation')
router.register(r'produits', views.ProduitViewSet, basename='produit')
router.register(r'reservations', views.ReservationViewSet, basename='reservation')
router.register(r'avis', views.AvisViewSet, basename='avis')
router.register(r'ia', views.IARecommandationViewSet, basename='ia-recommandation')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')
# Ajout des routes manquantes pour cohérence avec serializers/views/models
router.register(r'soins', views.SoinViewSet, basename='soin')
router.register(r'rendezvous', views.RendezVousViewSet, basename='rendezvous')
router.register(r'clients', views.ClientViewSet, basename='client')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

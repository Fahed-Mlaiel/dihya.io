"""
Dihya – Django eCommerce API Routes Ultra Avancé
------------------------------------------------
- Endpoints REST pour produits, catégories, commandes, paniers, paiements, livraisons, avis, promotions, IA recommandation, logs, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, multilingue, extensibilité
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST eCommerce (sécurité, multilingue, souveraineté)
🇬🇧 Django REST eCommerce routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للتجارة الإلكترونية (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n eCommerce (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'produits', views.ProduitViewSet, basename='produit')
router.register(r'categories', views.CategorieViewSet, basename='categorie')
router.register(r'commandes', views.CommandeViewSet, basename='commande')
router.register(r'paniers', views.PanierViewSet, basename='panier')
router.register(r'paiements', views.PaiementViewSet, basename='paiement')
router.register(r'livraisons', views.LivraisonViewSet, basename='livraison')
router.register(r'avis', views.AvisViewSet, basename='avis')
router.register(r'promotions', views.PromotionViewSet, basename='promotion')
router.register(r'ia', views.IARecommandationViewSet, basename='ia-recommandation')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

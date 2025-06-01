"""
Dihya – Django Assurance API Routes Ultra Avancé
-----------------------------------------------
- Endpoints REST pour contrats, souscriptions, sinistres, paiements, attestations, notifications, logs, audit
- Sécurité, RBAC, logs, conformité RGPD/NIS2, multilingue, extensibilité
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST assurance (sécurité, multilingue, souveraineté)
🇬🇧 Django REST insurance routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للتأمين (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n taamin (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'contrats', views.ContratViewSet, basename='contrat')
router.register(r'souscriptions', views.SouscriptionViewSet, basename='souscription')
router.register(r'sinistres', views.SinistreViewSet, basename='sinistre')
router.register(r'paiements', views.PaiementViewSet, basename='paiement')
router.register(r'attestations', views.AttestationViewSet, basename='attestation')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

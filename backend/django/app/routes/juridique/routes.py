"""
Dihya – Django Juridique API Routes Ultra Avancé
------------------------------------------------
- Endpoints REST pour contrats, documents, signatures, litiges, conformité, audits, IA juridique, logs, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, multilingue, extensibilité
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST juridique (sécurité, multilingue, souveraineté)
🇬🇧 Django REST legal routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST القانونية (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n tazult (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'contrats', views.ContratViewSet, basename='contrat')
router.register(r'documents', views.DocumentViewSet, basename='document')
router.register(r'signatures', views.SignatureViewSet, basename='signature')
router.register(r'litiges', views.LitigeViewSet, basename='litige')
router.register(r'conformite', views.ConformiteViewSet, basename='conformite')
router.register(r'audits', views.AuditViewSet, basename='audit')
router.register(r'ia', views.IAJuridiqueViewSet, basename='ia-juridique')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

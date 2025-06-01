"""
Dihya – Django Validators API Routes Ultra Avancé
-------------------------------------------------
- Endpoints REST pour validation emails, fichiers, schémas JSON/XML, identités, IBAN, SIRET, flux, uploads, IA validation, logs, rapports, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, anonymisation, multilingue, extensibilité, fallback IA open source
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST validators (sécurité, multilingue, souveraineté)
🇬🇧 Django REST validators routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للتحقق (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n usenqed (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'email', views.EmailValidatorViewSet, basename='email-validator')
router.register(r'file', views.FileValidatorViewSet, basename='file-validator')
router.register(r'schema', views.SchemaValidatorViewSet, basename='schema-validator')
router.register(r'identite', views.IdentiteValidatorViewSet, basename='identite-validator')
router.register(r'iban', views.IBANValidatorViewSet, basename='iban-validator')
router.register(r'siret', views.SIRETValidatorViewSet, basename='siret-validator')
router.register(r'flux', views.FluxValidatorViewSet, basename='flux-validator')
router.register(r'upload', views.UploadValidatorViewSet, basename='upload-validator')
router.register(r'ia', views.IAValidatorViewSet, basename='ia-validator')
router.register(r'logs', views.LogValidatorViewSet, basename='log-validator')
router.register(r'rapports', views.RapportViewSet, basename='rapport')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, anonymisation, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Fallback IA open source : tous les endpoints critiques disposent d’un fallback open source
# Extensible : ajoutez vos endpoints (validation, IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

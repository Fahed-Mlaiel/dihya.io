"""
Dihya – Django Sport API Routes Ultra Avancé
--------------------------------------------
- Endpoints REST pour clubs, équipes, athlètes, compétitions, résultats, entraînements, billetterie, IA sport, notifications, rapports, logs, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, anonymisation, multilingue, extensibilité, fallback IA open source
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST sport (sécurité, multilingue, souveraineté)
🇬🇧 Django REST sport routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للرياضة (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n urar (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'clubs', views.ClubViewSet, basename='club')
router.register(r'equipes', views.EquipeViewSet, basename='equipe')
router.register(r'athletes', views.AthleteViewSet, basename='athlete')
router.register(r'competitions', views.CompetitionViewSet, basename='competition')
router.register(r'resultats', views.ResultatViewSet, basename='resultat')
router.register(r'entrainements', views.EntrainementViewSet, basename='entrainement')
router.register(r'billetterie', views.BilletterieViewSet, basename='billetterie')
router.register(r'ia', views.IASportViewSet, basename='ia-sport')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'rapports', views.RapportViewSet, basename='rapport')
router.register(r'logs', views.LogSportViewSet, basename='log-sport')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, anonymisation, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Fallback IA open source : tous les endpoints critiques disposent d’un fallback open source
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

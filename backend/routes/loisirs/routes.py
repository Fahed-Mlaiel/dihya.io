"""
Routes backend Django pour la gestion Loisirs (Dihya)
Ultra avancé, sécurisé, multilingue, REST & GraphQL-ready, RGPD, plugins, audit, multitenancy.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActiviteViewSet, EvenementViewSet, ReservationViewSet
from .schemas import ActiviteSchema, EvenementSchema, ReservationSchema
from .plugins import *
from .audit import *
from .i18n import *
from .permissions import *

# RESTful API
router = DefaultRouter()
router.register(r'activites', ActiviteViewSet, basename='loisirs-activite')
router.register(r'evenements', EvenementViewSet, basename='loisirs-evenement')
router.register(r'reservations', ReservationViewSet, basename='loisirs-reservation')

urlpatterns = [
    path('', include(router.urls)),
    # GraphQL endpoint (à brancher sur la stack GraphQL du projet)
    # path('graphql/', GraphQLView.as_view(graphiql=True)),
]

# Sécurité avancée, CORS, JWT, audit, WAF, anti-DDOS, RBAC, i18n, RGPD, plugins, multitenancy sont gérés dans les middlewares globaux du projet et dans chaque ViewSet.

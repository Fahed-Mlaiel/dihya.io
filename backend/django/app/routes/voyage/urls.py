from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReservationViewSet, ItineraireViewSet

router = DefaultRouter()
router.register(r'reservations', ReservationViewSet, basename='voyage-reservation')
router.register(r'itineraires', ItineraireViewSet, basename='voyage-itineraire')

urlpatterns = [
    path('', include(router.urls)),
    # Endpoint RGPD export (à implémenter dans views avancées)
    # path('rgpd-export/', ... , name='voyage-rgpd-export'),
]

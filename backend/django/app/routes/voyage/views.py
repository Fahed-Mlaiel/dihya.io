from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Reservation, Itineraire
from .serializers import ReservationSerializer, ItineraireSerializer
from .permissions import IsReservationOwnerOrReadOnly, IsItineraireManagerOrReadOnly
from .audit import voyage_audit_logger
from .i18n import VOYAGE_I18N

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsReservationOwnerOrReadOnly]

    def perform_create(self, serializer):
        obj = serializer.save(user=self.request.user)
        voyage_audit_logger.log(self.request.user, 'create', 'Reservation', obj.id, details=obj.voyage, language=obj.lang)

    def perform_destroy(self, instance):
        voyage_audit_logger.log(self.request.user, 'delete', 'Reservation', instance.id, details=instance.voyage, language=instance.lang)
        instance.delete()

class ItineraireViewSet(viewsets.ModelViewSet):
    queryset = Itineraire.objects.all()
    serializer_class = ItineraireSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsItineraireManagerOrReadOnly]

    def perform_create(self, serializer):
        obj = serializer.save(manager=self.request.user)
        voyage_audit_logger.log(self.request.user, 'create', 'Itineraire', obj.id, details=f"{obj.depart} → {obj.arrivee}")

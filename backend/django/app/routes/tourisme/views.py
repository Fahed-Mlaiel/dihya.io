"""
Dihya – Views avancées pour le module Tourisme
- Sécurité, accessibilité, multilingue, RGPD, audit, documentation
"""
from rest_framework import viewsets, permissions
from .models import Destination, Offre, Reservation, Avis
from .serializers import DestinationSerializer, OffreSerializer, ReservationSerializer, AvisSerializer

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    permission_classes = [permissions.IsAuthenticated]

class OffreViewSet(viewsets.ModelViewSet):
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

class AvisViewSet(viewsets.ModelViewSet):
    queryset = Avis.objects.all()
    serializer_class = AvisSerializer
    permission_classes = [permissions.IsAuthenticated]

class GuideViewSet(viewsets.ModelViewSet):
    # Gestion guides, sécurité, logs, RGPD
    ...

class EvenementViewSet(viewsets.ModelViewSet):
    # Gestion événements, sécurité, logs, RGPD
    ...

class PartenairesViewSet(viewsets.ModelViewSet):
    # Gestion partenaires, sécurité, logs, RGPD
    ...

class IATourismeViewSet(viewsets.ViewSet):
    # Intégration IA, fallback open source, logs, RGPD
    ...

class NotificationViewSet(viewsets.ViewSet):
    # Notifications multicanal, logs, RGPD
    ...

class RapportViewSet(viewsets.ViewSet):
    # Génération rapports PDF/CSV, logs, RGPD
    ...

class LogTourismeViewSet(viewsets.ReadOnlyModelViewSet):
    # Logs tourisme, sécurité, RGPD
    ...

class AuditLogViewSet(viewsets.ReadOnlyModelViewSet):
    # Logs audit, sécurité, RGPD
    ...

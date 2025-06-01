"""
Dihya – Views avancées pour le module Services à la Personne
- Sécurité, accessibilité, multilingue, RGPD, audit, documentation
"""
from rest_framework import viewsets, permissions
from .models import Beneficiaire, Intervenant, Prestation
from .serializers import BeneficiaireSerializer, IntervenantSerializer, PrestationSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Beneficiaire.objects.all()
    serializer_class = BeneficiaireSerializer
    permission_classes = [permissions.IsAuthenticated]

class IntervenantViewSet(viewsets.ModelViewSet):
    queryset = Intervenant.objects.all()
    serializer_class = IntervenantSerializer
    permission_classes = [permissions.IsAuthenticated]

class PrestationViewSet(viewsets.ModelViewSet):
    queryset = Prestation.objects.all()
    serializer_class = PrestationSerializer
    permission_classes = [permissions.IsAuthenticated]

class PlanningViewSet(viewsets.ModelViewSet):
    # Gestion planning, sécurité, logs, RGPD
    ...

class ReservationViewSet(viewsets.ModelViewSet):
    # Gestion réservations, sécurité, logs, RGPD
    ...

class FactureViewSet(viewsets.ModelViewSet):
    # Gestion factures, sécurité, logs, RGPD
    ...

class AvisViewSet(viewsets.ModelViewSet):
    # Gestion avis, sécurité, logs, RGPD
    ...

class IAServicesViewSet(viewsets.ViewSet):
    # Intégration IA, fallback open source, logs, RGPD
    ...

class NotificationViewSet(viewsets.ViewSet):
    # Notifications multicanal, logs, RGPD
    ...

class RapportViewSet(viewsets.ViewSet):
    # Génération rapports PDF/CSV, logs, RGPD
    ...

class AuditLogViewSet(viewsets.ReadOnlyModelViewSet):
    # Logs audit, sécurité, RGPD
    ...

# TODO: Implémenter les méthodes manquantes pour chaque ViewSet avancé

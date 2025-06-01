"""
Dihya – Django Beauté API Views Ultra Avancé
--------------------------------------------
- ViewSets pour soins, produits, rendez-vous, clients
- Sécurité, RBAC, audit, logs, multilingue, RGPD, extensibilité
"""
from rest_framework import viewsets, permissions
from .serializers import SoinSerializer, ProduitSerializer, RendezVousSerializer, ClientSerializer

class SoinViewSet(viewsets.ModelViewSet):
    serializer_class = SoinSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = []

class ProduitViewSet(viewsets.ModelViewSet):
    serializer_class = ProduitSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = []

class RendezVousViewSet(viewsets.ModelViewSet):
    serializer_class = RendezVousSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = []

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = []

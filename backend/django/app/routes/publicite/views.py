"""
Dihya – Vues Django REST pour le module Publicité
- Sécurité, RBAC, accessibilité, RGPD
"""
from rest_framework import viewsets, permissions
from .models import CampagnePublicitaire, AnalyticsPublicite
from .serializers import CampagnePublicitaireSerializer, AnalyticsPubliciteSerializer
from .permissions import IsPubliciteAdminOrReadOnly

class CampagnePublicitaireViewSet(viewsets.ModelViewSet):
    queryset = CampagnePublicitaire.objects.all()
    serializer_class = CampagnePublicitaireSerializer
    permission_classes = [IsPubliciteAdminOrReadOnly]

class AnalyticsPubliciteViewSet(viewsets.ModelViewSet):
    queryset = AnalyticsPublicite.objects.all()
    serializer_class = AnalyticsPubliciteSerializer
    permission_classes = [IsPubliciteAdminOrReadOnly]

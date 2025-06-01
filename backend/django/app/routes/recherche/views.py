"""
Dihya – Vues Django REST pour le module Recherche
- Sécurité, RBAC, accessibilité, RGPD
"""
from rest_framework import viewsets, permissions
from .models import RequeteRecherche, ResultatRecherche
from .serializers import RequeteRechercheSerializer, ResultatRechercheSerializer
from .permissions import IsRechercheAdminOrReadOnly

class RequeteRechercheViewSet(viewsets.ModelViewSet):
    queryset = RequeteRecherche.objects.all()
    serializer_class = RequeteRechercheSerializer
    permission_classes = [IsRechercheAdminOrReadOnly]

class ResultatRechercheViewSet(viewsets.ModelViewSet):
    queryset = ResultatRecherche.objects.all()
    serializer_class = ResultatRechercheSerializer
    permission_classes = [IsRechercheAdminOrReadOnly]

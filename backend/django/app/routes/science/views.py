"""
Dihya – Vues Django REST pour le module Science
- Sécurité, RBAC, accessibilité, RGPD
"""
from rest_framework import viewsets, permissions
from .models import ProjetScientifique, Publication, Chercheur
from .serializers import ProjetScientifiqueSerializer, PublicationSerializer, ChercheurSerializer
from .permissions import IsScienceAdminOrReadOnly

class ProjetScientifiqueViewSet(viewsets.ModelViewSet):
    queryset = ProjetScientifique.objects.all()
    serializer_class = ProjetScientifiqueSerializer
    permission_classes = [IsScienceAdminOrReadOnly]

class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = [IsScienceAdminOrReadOnly]

class ChercheurViewSet(viewsets.ModelViewSet):
    queryset = Chercheur.objects.all()
    serializer_class = ChercheurSerializer
    permission_classes = [IsScienceAdminOrReadOnly]

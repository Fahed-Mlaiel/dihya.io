"""
Dihya – Vues Django REST pour le module Mode
- Sécurité, RBAC, accessibilité, RGPD
"""
from rest_framework import viewsets, permissions
from .models import Collection, Produit, Createur
from .serializers import CollectionSerializer, ProduitSerializer, CreateurSerializer
from .permissions import IsModeAdminOrReadOnly

class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [IsModeAdminOrReadOnly]

class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer
    permission_classes = [IsModeAdminOrReadOnly]

class CreateurViewSet(viewsets.ModelViewSet):
    queryset = Createur.objects.all()
    serializer_class = CreateurSerializer
    permission_classes = [IsModeAdminOrReadOnly]

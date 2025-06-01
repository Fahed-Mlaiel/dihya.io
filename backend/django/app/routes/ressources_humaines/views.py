"""
Dihya – Vues Django REST pour le module Ressources Humaines
- Sécurité, RBAC, accessibilité, RGPD
"""
from rest_framework import viewsets, permissions
from .models import Employe, Poste, Candidature
from .serializers import EmployeSerializer, PosteSerializer, CandidatureSerializer
from .permissions import IsRHAdminOrReadOnly

class EmployeViewSet(viewsets.ModelViewSet):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer
    permission_classes = [IsRHAdminOrReadOnly]

class PosteViewSet(viewsets.ModelViewSet):
    queryset = Poste.objects.all()
    serializer_class = PosteSerializer
    permission_classes = [IsRHAdminOrReadOnly]

class CandidatureViewSet(viewsets.ModelViewSet):
    queryset = Candidature.objects.all()
    serializer_class = CandidatureSerializer
    permission_classes = [IsRHAdminOrReadOnly]

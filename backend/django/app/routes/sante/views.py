"""
Dihya – Vues Django REST pour le module Santé
- Sécurité, RBAC, accessibilité, RGPD
"""
from rest_framework import viewsets, permissions
from .models import Patient, RendezVous, DossierMedical
from .serializers import PatientSerializer, RendezVousSerializer, DossierMedicalSerializer
from .permissions import IsSanteAdminOrReadOnly

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsSanteAdminOrReadOnly]

class RendezVousViewSet(viewsets.ModelViewSet):
    queryset = RendezVous.objects.all()
    serializer_class = RendezVousSerializer
    permission_classes = [IsSanteAdminOrReadOnly]

class DossierMedicalViewSet(viewsets.ModelViewSet):
    queryset = DossierMedical.objects.all()
    serializer_class = DossierMedicalSerializer
    permission_classes = [IsSanteAdminOrReadOnly]

"""
Views Health (API ultra avancée, sécurité, accessibilité, multilingue)
"""
from rest_framework import viewsets
from .models import DossierSante
from .serializers import DossierSanteSerializer
from .permissions import IsMedecinOrOwner

class DossierSanteViewSet(viewsets.ModelViewSet):
    queryset = DossierSante.objects.all()
    serializer_class = DossierSanteSerializer
    permission_classes = [IsMedecinOrOwner]

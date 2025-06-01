"""
Views Juridique (API ultra avancée, sécurité, accessibilité, multilingue)
"""
from rest_framework import viewsets
from .models import DossierJuridique
from .serializers import DossierJuridiqueSerializer
from .permissions import IsResponsable

class DossierJuridiqueViewSet(viewsets.ModelViewSet):
    queryset = DossierJuridique.objects.all()
    serializer_class = DossierJuridiqueSerializer
    permission_classes = [IsResponsable]

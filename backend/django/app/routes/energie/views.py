"""
Views Énergie (API ultra avancée, sécurité, accessibilité, multilingue)
"""
from rest_framework import viewsets
from .models import SiteEnergie
from .serializers import SiteEnergieSerializer
from .permissions import IsResponsable

class SiteEnergieViewSet(viewsets.ModelViewSet):
    queryset = SiteEnergie.objects.all()
    serializer_class = SiteEnergieSerializer
    permission_classes = [IsResponsable]

"""
Views Construction (API ultra avancée, sécurité, accessibilité, multilingue)
"""
from rest_framework import viewsets
from .models import Chantier
from .serializers import ChantierSerializer
from .permissions import IsChefChantier

class ChantierViewSet(viewsets.ModelViewSet):
    queryset = Chantier.objects.all()
    serializer_class = ChantierSerializer
    permission_classes = [IsChefChantier]

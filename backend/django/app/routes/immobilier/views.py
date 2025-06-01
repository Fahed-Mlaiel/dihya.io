"""
Views Immobilier (API ultra avancée, sécurité, accessibilité, multilingue)
"""
from rest_framework import viewsets
from .models import BienImmobilier
from .serializers import BienImmobilierSerializer
from .permissions import IsProprietaire

class BienImmobilierViewSet(viewsets.ModelViewSet):
    queryset = BienImmobilier.objects.all()
    serializer_class = BienImmobilierSerializer
    permission_classes = [IsProprietaire]

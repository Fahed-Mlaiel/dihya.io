"""
Views Gamer (API ultra avancée, sécurité, accessibilité, multilingue)
"""
from rest_framework import viewsets
from .models import ProfilGamer
from .serializers import ProfilGamerSerializer
from .permissions import IsOwner

class ProfilGamerViewSet(viewsets.ModelViewSet):
    queryset = ProfilGamer.objects.all()
    serializer_class = ProfilGamerSerializer
    permission_classes = [IsOwner]

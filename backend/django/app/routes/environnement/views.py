"""
Views Environnement (API ultra avancée, sécurité, accessibilité, multilingue)
"""
from rest_framework import viewsets
from .models import SiteEnvironnement
from .serializers import SiteEnvironnementSerializer
from .permissions import IsResponsable

class SiteEnvironnementViewSet(viewsets.ModelViewSet):
    queryset = SiteEnvironnement.objects.all()
    serializer_class = SiteEnvironnementSerializer
    permission_classes = [IsResponsable]

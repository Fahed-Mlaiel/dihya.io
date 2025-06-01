"""
Views Éducation (API ultra avancée, sécurité, accessibilité, multilingue)
"""
from rest_framework import viewsets
from .models import Etablissement
from .serializers import EtablissementSerializer
from .permissions import IsResponsable

class EtablissementViewSet(viewsets.ModelViewSet):
    queryset = Etablissement.objects.all()
    serializer_class = EtablissementSerializer
    permission_classes = [IsResponsable]

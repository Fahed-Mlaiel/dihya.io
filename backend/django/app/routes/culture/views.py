"""
Views Culture (API ultra avancée, sécurité, accessibilité, multilingue)
"""
from rest_framework import viewsets
from .models import EvenementCulturel
from .serializers import EvenementCulturelSerializer
from .permissions import IsOrganisateur

class EvenementCulturelViewSet(viewsets.ModelViewSet):
    queryset = EvenementCulturel.objects.all()
    serializer_class = EvenementCulturelSerializer
    permission_classes = [IsOrganisateur]

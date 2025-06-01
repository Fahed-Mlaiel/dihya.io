"""
Views Loisirs (API ultra avancée, sécurité, accessibilité, multilingue)
"""
from rest_framework import viewsets
from .models import ActiviteLoisir
from .serializers import ActiviteLoisirSerializer
from .permissions import IsResponsable

class ActiviteLoisirViewSet(viewsets.ModelViewSet):
    queryset = ActiviteLoisir.objects.all()
    serializer_class = ActiviteLoisirSerializer
    permission_classes = [IsResponsable]

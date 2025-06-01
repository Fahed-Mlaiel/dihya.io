"""
Views Hôtellerie (API ultra avancée, sécurité, accessibilité, multilingue)
"""
from rest_framework import viewsets
from .models import Hotel
from .serializers import HotelSerializer
from .permissions import IsResponsable

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsResponsable]

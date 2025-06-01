"""
Dihya – Vues Django REST pour le module Médias
- Sécurité, RBAC, accessibilité, RGPD
"""
from rest_framework import viewsets, permissions
from .models import Media
from .serializers import MediaSerializer
from .permissions import IsMediaAdminOrReadOnly

class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    permission_classes = [IsMediaAdminOrReadOnly]

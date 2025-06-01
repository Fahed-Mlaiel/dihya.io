"""
Dihya – Vues Django REST pour le module Preview
- Sécurité, RBAC, accessibilité, RGPD
"""
from rest_framework import viewsets, permissions
from .models import Preview
from .serializers import PreviewSerializer
from .permissions import IsPreviewAdminOrReadOnly

class PreviewViewSet(viewsets.ModelViewSet):
    queryset = Preview.objects.all()
    serializer_class = PreviewSerializer
    permission_classes = [IsPreviewAdminOrReadOnly]

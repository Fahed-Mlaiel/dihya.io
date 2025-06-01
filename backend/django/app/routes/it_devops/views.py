"""
Views IT & DevOps (API ultra avancée, sécurité, accessibilité, multilingue)
"""
from rest_framework import viewsets
from .models import Pipeline
from .serializers import PipelineSerializer
from .permissions import IsResponsable

class PipelineViewSet(viewsets.ModelViewSet):
    queryset = Pipeline.objects.all()
    serializer_class = PipelineSerializer
    permission_classes = [IsResponsable]

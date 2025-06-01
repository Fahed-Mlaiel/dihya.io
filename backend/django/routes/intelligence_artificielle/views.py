"""
Vues Django REST & GraphQL pour la gestion des projets d'intelligence artificielle.
Sécurité maximale, multilingue, multitenant, extensible, RGPD-ready.
"""
from typing import Any
from django.utils.translation import gettext_lazy as _
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .serializers import IAProjectSerializer
from .models import IAProject
from .permissions import IsAdminOrReadOnly
from .audit import audit_log_action
from .utils import get_current_tenant

class IAProjectViewSet(viewsets.ModelViewSet):
    """
    API avancée pour la gestion des projets IA (REST & GraphQL-ready).
    """
    queryset = IAProject.objects.all()
    serializer_class = IAProjectSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        tenant = get_current_tenant(self.request)
        return IAProject.objects.filter(tenant=tenant)

    def perform_create(self, serializer):
        tenant = get_current_tenant(self.request)
        instance = serializer.save(tenant=tenant, created_by=self.request.user)
        audit_log_action(self.request.user, _('Création projet IA'), instance)

    def perform_update(self, serializer):
        instance = serializer.save()
        audit_log_action(self.request.user, _('Mise à jour projet IA'), instance)

    def perform_destroy(self, instance):
        audit_log_action(self.request.user, _('Suppression projet IA'), instance)
        instance.delete()

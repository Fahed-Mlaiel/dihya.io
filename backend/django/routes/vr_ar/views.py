"""
Vues Django REST & GraphQL pour la gestion des projets VR/AR.
Sécurité maximale, multilingue, multitenant, extensible, RGPD-ready.
"""
from typing import Any
from django.utils.translation import gettext_lazy as _
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .serializers import VRARProjectSerializer
from .models import VRARProject
from .permissions import IsAdminOrReadOnly
from .audit import audit_log_action
from .utils import get_current_tenant

class VRARProjectViewSet(viewsets.ModelViewSet):
    """
    API avancée pour la gestion des projets VR/AR (REST & GraphQL-ready).
    """
    queryset = VRARProject.objects.all()
    serializer_class = VRARProjectSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        tenant = get_current_tenant(self.request)
        return VRARProject.objects.filter(tenant=tenant)

    def perform_create(self, serializer):
        tenant = get_current_tenant(self.request)
        instance = serializer.save(tenant=tenant, created_by=self.request.user)
        audit_log_action(self.request.user, _('Création projet VR/AR'), instance)

    def perform_update(self, serializer):
        instance = serializer.save()
        audit_log_action(self.request.user, _('Mise à jour projet VR/AR'), instance)

    def perform_destroy(self, instance):
        audit_log_action(self.request.user, _('Suppression projet VR/AR'), instance)
        instance.delete()

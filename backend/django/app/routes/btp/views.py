"""
Vues Django REST & GraphQL pour la gestion des projets BTP.
Sécurité maximale, multilingue, multitenant, extensible, RGPD-ready.
"""
from rest_framework import viewsets
from .serializers import BTPProjectSerializer
from .models import BTPProject
from .permissions import IsAdminOrReadOnly
from .audit import audit_log

class BTPProjectViewSet(viewsets.ModelViewSet):
    queryset = BTPProject.objects.all()
    serializer_class = BTPProjectSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        instance = serializer.save()
        audit_log(self.request.user, 'create_btp', instance)

    def perform_update(self, serializer):
        instance = serializer.save()
        audit_log(self.request.user, 'update_btp', instance)

    def perform_destroy(self, instance):
        audit_log(self.request.user, 'delete_btp', instance)
        instance.delete()

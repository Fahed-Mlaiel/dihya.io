"""
Vues RESTful et GraphQL pour la gestion de projets de construction (génie civil, architecture, etc.)
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Construction
from .serializers import ConstructionSerializer
from .plugins import get_plugins
from .ia import llama_fallback
from .audit import log_action
from .utils import export_projects_zip
from django.utils.translation import gettext_lazy as _
from graphql import GraphQLError

class ConstructionListView(generics.ListCreateAPIView):
    """Liste et création de projets construction (RESTful, sécurisé, multilingue, multitenant)"""
    queryset = Construction.objects.all()
    serializer_class = ConstructionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        tenant = self.request.headers.get('X-TENANT', 'default')
        return Construction.objects.filter(tenant=tenant)

    def list(self, request, *args, **kwargs):
        log_action(request, 'list', 'construction')
        return super().list(request, *args, **kwargs)

class ConstructionDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Détail, modification, suppression d'un projet construction (RESTful, sécurisé, multilingue, multitenant)"""
    queryset = Construction.objects.all()
    serializer_class = ConstructionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        tenant = self.request.headers.get('X-TENANT', 'default')
        return Construction.objects.filter(tenant=tenant)

    def retrieve(self, request, *args, **kwargs):
        log_action(request, 'retrieve', 'construction')
        return super().retrieve(request, *args, **kwargs)

class ConstructionExportView(APIView):
    """Export des projets construction (RGPD, audit, multitenant)"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tenant = request.headers.get('X-TENANT', 'default')
        log_action(request, 'export', 'construction')
        return export_projects_zip(Construction, tenant)

class ConstructionPluginListView(APIView):
    """Liste des plugins construction (extensible, audit)"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        log_action(request, 'list_plugins', 'construction')
        return Response(get_plugins('construction'))

class ConstructionIAView(APIView):
    """Intégration IA fallback (LLaMA, Mixtral, Mistral)"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        prompt = request.data.get('prompt', '')
        result = llama_fallback(prompt)
        log_action(request, 'ia_fallback', 'construction')
        return Response({'result': result})

# GraphQL (exemple minimal, à étendre)
import graphene
class ConstructionType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()

class Query(graphene.ObjectType):
    construction = graphene.Field(ConstructionType, id=graphene.Int())
    all_construction = graphene.List(ConstructionType)

    def resolve_construction(self, info, id):
        try:
            obj = Construction.objects.get(pk=id)
            return ConstructionType(id=obj.id, name=obj.name, description=obj.description)
        except Construction.DoesNotExist:
            raise GraphQLError(_('Projet construction introuvable'))

    def resolve_all_construction(self, info):
        return [ConstructionType(id=obj.id, name=obj.name, description=obj.description) for obj in Construction.objects.all()]

schema = graphene.Schema(query=Query)

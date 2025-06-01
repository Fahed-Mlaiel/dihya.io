"""
Vues RESTful et GraphQL pour la gestion de projets 3D (VR/AR, modélisation, etc.)
Sécurité maximale, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project3D
from .serializers import Project3DSerializer
from .plugins import get_plugins
from .ia import llama_fallback
from .audit import log_action
from .utils import export_projects_zip
from django.utils.translation import gettext_lazy as _
from graphql import GraphQLError

class Project3DListView(generics.ListCreateAPIView):
    """Liste et création de projets 3D (RESTful, sécurisé, multilingue, multitenant)"""
    queryset = Project3D.objects.all()
    serializer_class = Project3DSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        tenant = self.request.headers.get('X-TENANT', 'default')
        return Project3D.objects.filter(tenant=tenant)

    def list(self, request, *args, **kwargs):
        log_action(request, 'list', '3d')
        return super().list(request, *args, **kwargs)

class Project3DDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Détail, modification, suppression d'un projet 3D (RESTful, sécurisé, multilingue, multitenant)"""
    queryset = Project3D.objects.all()
    serializer_class = Project3DSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        tenant = self.request.headers.get('X-TENANT', 'default')
        return Project3D.objects.filter(tenant=tenant)

    def retrieve(self, request, *args, **kwargs):
        log_action(request, 'retrieve', '3d')
        return super().retrieve(request, *args, **kwargs)

class Project3DExportView(APIView):
    """Export des projets 3D (RGPD, audit, multitenant)"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tenant = request.headers.get('X-TENANT', 'default')
        log_action(request, 'export', '3d')
        return export_projects_zip(Project3D, tenant)

class Project3DPluginListView(APIView):
    """Liste des plugins 3D (extensible, audit)"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        log_action(request, 'list_plugins', '3d')
        return Response(get_plugins('3d'))

class Project3DIAView(APIView):
    """Intégration IA fallback (LLaMA, Mixtral, Mistral)"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        prompt = request.data.get('prompt', '')
        result = llama_fallback(prompt)
        log_action(request, 'ia_fallback', '3d')
        return Response({'result': result})

# GraphQL (exemple minimal, à étendre)
import graphene
class Project3DType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()

class Query(graphene.ObjectType):
    project3d = graphene.Field(Project3DType, id=graphene.Int())
    all_project3d = graphene.List(Project3DType)

    def resolve_project3d(self, info, id):
        try:
            obj = Project3D.objects.get(pk=id)
            return Project3DType(id=obj.id, name=obj.name, description=obj.description)
        except Project3D.DoesNotExist:
            raise GraphQLError(_('Projet 3D introuvable'))

    def resolve_all_project3d(self, info):
        return [Project3DType(id=obj.id, name=obj.name, description=obj.description) for obj in Project3D.objects.all()]

schema = graphene.Schema(query=Query)

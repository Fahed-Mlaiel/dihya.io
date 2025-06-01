"""
Vues RESTful et GraphQL pour la gestion de projets d'assurance (santé, auto, habitation, etc.)
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Assurance
from .serializers import AssuranceSerializer
from .plugins import get_plugins
from .ia import llama_fallback
from .audit import log_action
from .utils import export_projects_zip
from django.utils.translation import gettext_lazy as _
from graphql import GraphQLError

class AssuranceListView(generics.ListCreateAPIView):
    """Liste et création de projets assurance (RESTful, sécurisé, multilingue, multitenant)"""
    queryset = Assurance.objects.all()
    serializer_class = AssuranceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        tenant = self.request.headers.get('X-TENANT', 'default')
        return Assurance.objects.filter(tenant=tenant)

    def list(self, request, *args, **kwargs):
        log_action(request, 'list', 'assurance')
        return super().list(request, *args, **kwargs)

class AssuranceDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Détail, modification, suppression d'un projet assurance (RESTful, sécurisé, multilingue, multitenant)"""
    queryset = Assurance.objects.all()
    serializer_class = AssuranceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        tenant = self.request.headers.get('X-TENANT', 'default')
        return Assurance.objects.filter(tenant=tenant)

    def retrieve(self, request, *args, **kwargs):
        log_action(request, 'retrieve', 'assurance')
        return super().retrieve(request, *args, **kwargs)

class AssuranceExportView(APIView):
    """Export des projets assurance (RGPD, audit, multitenant)"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tenant = request.headers.get('X-TENANT', 'default')
        log_action(request, 'export', 'assurance')
        return export_projects_zip(Assurance, tenant)

class AssurancePluginListView(APIView):
    """Liste des plugins assurance (extensible, audit)"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        log_action(request, 'list_plugins', 'assurance')
        return Response(get_plugins('assurance'))

class AssuranceIAView(APIView):
    """Intégration IA fallback (LLaMA, Mixtral, Mistral)"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        prompt = request.data.get('prompt', '')
        result = llama_fallback(prompt)
        log_action(request, 'ia_fallback', 'assurance')
        return Response({'result': result})

# GraphQL (exemple minimal, à étendre)
import graphene
class AssuranceType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()

class Query(graphene.ObjectType):
    assurance = graphene.Field(AssuranceType, id=graphene.Int())
    all_assurance = graphene.List(AssuranceType)

    def resolve_assurance(self, info, id):
        try:
            obj = Assurance.objects.get(pk=id)
            return AssuranceType(id=obj.id, name=obj.name, description=obj.description)
        except Assurance.DoesNotExist:
            raise GraphQLError(_('Projet assurance introuvable'))

    def resolve_all_assurance(self, info):
        return [AssuranceType(id=obj.id, name=obj.name, description=obj.description) for obj in Assurance.objects.all()]

schema = graphene.Schema(query=Query)

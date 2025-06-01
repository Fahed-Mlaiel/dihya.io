"""
Vues RESTful et GraphQL pour la gestion de projets beauté (cosmétique, bien-être, etc.)
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Beaute
from .serializers import BeauteSerializer
from .plugins import get_plugins
from .ia import llama_fallback
from .audit import log_action
from .utils import export_projects_zip
from django.utils.translation import gettext_lazy as _
from graphql import GraphQLError

class BeauteListView(generics.ListCreateAPIView):
    """Liste et création de projets beauté (RESTful, sécurisé, multilingue, multitenant)"""
    queryset = Beaute.objects.all()
    serializer_class = BeauteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        tenant = self.request.headers.get('X-TENANT', 'default')
        return Beaute.objects.filter(tenant=tenant)

    def list(self, request, *args, **kwargs):
        log_action(request, 'list', 'beaute')
        return super().list(request, *args, **kwargs)

class BeauteDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Détail, modification, suppression d'un projet beauté (RESTful, sécurisé, multilingue, multitenant)"""
    queryset = Beaute.objects.all()
    serializer_class = BeauteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        tenant = self.request.headers.get('X-TENANT', 'default')
        return Beaute.objects.filter(tenant=tenant)

    def retrieve(self, request, *args, **kwargs):
        log_action(request, 'retrieve', 'beaute')
        return super().retrieve(request, *args, **kwargs)

class BeauteExportView(APIView):
    """Export des projets beauté (RGPD, audit, multitenant)"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tenant = request.headers.get('X-TENANT', 'default')
        log_action(request, 'export', 'beaute')
        return export_projects_zip(Beaute, tenant)

class BeautePluginListView(APIView):
    """Liste des plugins beauté (extensible, audit)"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        log_action(request, 'list_plugins', 'beaute')
        return Response(get_plugins('beaute'))

class BeauteIAView(APIView):
    """Intégration IA fallback (LLaMA, Mixtral, Mistral)"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        prompt = request.data.get('prompt', '')
        result = llama_fallback(prompt)
        log_action(request, 'ia_fallback', 'beaute')
        return Response({'result': result})

# GraphQL (exemple minimal, à étendre)
import graphene
class BeauteType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()

class Query(graphene.ObjectType):
    beaute = graphene.Field(BeauteType, id=graphene.Int())
    all_beaute = graphene.List(BeauteType)

    def resolve_beaute(self, info, id):
        try:
            obj = Beaute.objects.get(pk=id)
            return BeauteType(id=obj.id, name=obj.name, description=obj.description)
        except Beaute.DoesNotExist:
            raise GraphQLError(_('Projet beauté introuvable'))

    def resolve_all_beaute(self, info):
        return [BeauteType(id=obj.id, name=obj.name, description=obj.description) for obj in Beaute.objects.all()]

schema = graphene.Schema(query=Query)

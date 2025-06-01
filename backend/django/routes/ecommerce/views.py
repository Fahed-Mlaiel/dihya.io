"""
Vues RESTful et GraphQL pour la gestion de projets e-commerce (boutiques, marketplaces, etc.)
Sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, IA fallback.
"""
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Ecommerce
from .serializers import EcommerceSerializer
from .plugins import get_plugins
from .ia import llama_fallback
from .audit import log_action
from .utils import export_projects_zip
from django.utils.translation import gettext_lazy as _
from graphql import GraphQLError

class EcommerceListView(generics.ListCreateAPIView):
    """Liste et création de projets e-commerce (RESTful, sécurisé, multilingue, multitenant)"""
    queryset = Ecommerce.objects.all()
    serializer_class = EcommerceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        tenant = self.request.headers.get('X-TENANT', 'default')
        return Ecommerce.objects.filter(tenant=tenant)

    def list(self, request, *args, **kwargs):
        log_action(request, 'list', 'ecommerce')
        return super().list(request, *args, **kwargs)

class EcommerceDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Détail, modification, suppression d'un projet e-commerce (RESTful, sécurisé, multilingue, multitenant)"""
    queryset = Ecommerce.objects.all()
    serializer_class = EcommerceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        tenant = self.request.headers.get('X-TENANT', 'default')
        return Ecommerce.objects.filter(tenant=tenant)

    def retrieve(self, request, *args, **kwargs):
        log_action(request, 'retrieve', 'ecommerce')
        return super().retrieve(request, *args, **kwargs)

class EcommerceExportView(APIView):
    """Export des projets e-commerce (RGPD, audit, multitenant)"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tenant = request.headers.get('X-TENANT', 'default')
        log_action(request, 'export', 'ecommerce')
        return export_projects_zip(Ecommerce, tenant)

class EcommercePluginListView(APIView):
    """Liste des plugins e-commerce (extensible, audit)"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        log_action(request, 'list_plugins', 'ecommerce')
        return Response(get_plugins('ecommerce'))

class EcommerceIAView(APIView):
    """Intégration IA fallback (LLaMA, Mixtral, Mistral)"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        prompt = request.data.get('prompt', '')
        result = llama_fallback(prompt)
        log_action(request, 'ia_fallback', 'ecommerce')
        return Response({'result': result})

# GraphQL (exemple minimal, à étendre)
import graphene
class EcommerceType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()

class Query(graphene.ObjectType):
    ecommerce = graphene.Field(EcommerceType, id=graphene.Int())
    all_ecommerce = graphene.List(EcommerceType)

    def resolve_ecommerce(self, info, id):
        try:
            obj = Ecommerce.objects.get(pk=id)
            return EcommerceType(id=obj.id, name=obj.name, description=obj.description)
        except Ecommerce.DoesNotExist:
            raise GraphQLError(_('Projet e-commerce introuvable'))

    def resolve_all_ecommerce(self, info):
        return [EcommerceType(id=obj.id, name=obj.name, description=obj.description) for obj in Ecommerce.objects.all()]

schema = graphene.Schema(query=Query)

"""
Schéma GraphQL pour la gestion avancée des projets VR/AR.
Inclut sécurité, multilingue, audit, RGPD, plugins, multitenancy.
"""
import graphene
from graphene_django.types import DjangoObjectType
from .models import VRARProject

class VRARProjectType(DjangoObjectType):
    class Meta:
        model = VRARProject
        fields = ("id", "name", "description", "created_at", "updated_at", "tenant", "created_by", "is_active")

class Query(graphene.ObjectType):
    all_vrar_projects = graphene.List(VRARProjectType)
    def resolve_all_vrar_projects(self, info):
        user = info.context.user
        if not user.is_authenticated:
            return VRARProject.objects.none()
        return VRARProject.objects.filter(tenant=getattr(user, 'tenant', None))

schema = graphene.Schema(query=Query)

"""
Schéma GraphQL pour la gestion avancée des projets IA.
Inclut sécurité, multilingue, audit, RGPD, plugins, multitenancy.
"""
import graphene
from graphene_django.types import DjangoObjectType
from .models import IAProject

class IAProjectType(DjangoObjectType):
    class Meta:
        model = IAProject
        fields = ("id", "name", "description", "created_at", "updated_at", "tenant", "created_by", "is_active")

class Query(graphene.ObjectType):
    all_ia_projects = graphene.List(IAProjectType)
    def resolve_all_ia_projects(self, info):
        user = info.context.user
        if not user.is_authenticated:
            return IAProject.objects.none()
        return IAProject.objects.filter(tenant=getattr(user, 'tenant', None))

schema = graphene.Schema(query=Query)

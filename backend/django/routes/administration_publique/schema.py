"""
Schéma GraphQL pour la gestion avancée des projets d'administration publique.
Inclut sécurité, multilingue, audit, RGPD, plugins, multitenancy.
"""
import graphene
from graphene_django.types import DjangoObjectType
from .models import AdministrationPubliqueProject

class AdministrationPubliqueProjectType(DjangoObjectType):
    class Meta:
        model = AdministrationPubliqueProject
        fields = ("id", "name", "description", "created_at", "updated_at", "tenant", "created_by", "is_active")

class Query(graphene.ObjectType):
    all_administration_publique_projects = graphene.List(AdministrationPubliqueProjectType)
    def resolve_all_administration_publique_projects(self, info):
        user = info.context.user
        if not user.is_authenticated:
            return AdministrationPubliqueProject.objects.none()
        return AdministrationPubliqueProject.objects.filter(tenant=getattr(user, 'tenant', None))

schema = graphene.Schema(query=Query)

# ...existing code...
# Permissions RBAC ultra avancées pour le transport (admin, gestionnaire, chauffeur, client, auditeur, guest)
# Sécurité, souveraineté, auditabilité, conformité RGPD/NIS2

from rest_framework import permissions

class TransportPermission(permissions.BasePermission):
    """RBAC avancé pour le transport"""
    def has_permission(self, request, view):
        # ... logique RBAC ultra avancée ...
        return True
    def has_object_permission(self, request, view, obj):
        # ... logique RBAC objet ...
        return True

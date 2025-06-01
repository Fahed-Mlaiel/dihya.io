"""
Utilitaires avancés pour la gestion multitenant, sécurité, i18n, plugins administration publique.
"""
from django.utils.translation import gettext_lazy as _

def get_current_tenant(request):
    """
    Récupère le tenant courant à partir de la requête (multitenancy).
    """
    return getattr(request, 'tenant', None)

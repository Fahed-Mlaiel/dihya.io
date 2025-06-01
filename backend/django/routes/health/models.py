"""
Modèles avancés pour la gestion des projets santé (hôpitaux, cliniques, etc.).
Inclut multitenancy, audit, RGPD, multilingue, sécurité.
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class HealthProject(models.Model):
    """
    Modèle de projet santé avec gestion multitenant, audit, RGPD.
    """
    name = models.CharField(max_length=255, verbose_name=_('Nom du projet'))
    description = models.TextField(verbose_name=_('Description'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Créé le'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Mis à jour le'))
    tenant = models.ForeignKey('core.Tenant', on_delete=models.CASCADE, related_name='health_projects', verbose_name=_('Tenant'))
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name=_('Créé par'))
    is_active = models.BooleanField(default=True, verbose_name=_('Actif'))
    class Meta:
        verbose_name = _('Projet santé')
        verbose_name_plural = _('Projets santé')
        permissions = [
            ("export_health_project", "Peut exporter les projets santé (RGPD)")
        ]
    def __str__(self):
        return self.name

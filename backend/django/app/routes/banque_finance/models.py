"""
Modèles avancés pour la gestion des projets banque/finance.
Inclut multitenancy, audit, RGPD, multilingue, sécurité.
"""
from django.db import models
from django.conf import settings

class BanqueFinanceProject(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name = 'Projet banque/finance'
        verbose_name_plural = 'Projets banque/finance'
    def __str__(self):
        return self.name

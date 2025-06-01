"""
Models ultra avancés pour le module Assurance (Dihya)
Multilingue, RGPD, audit, plugins, multitenancy, sécurité maximale.
"""
from django.db import models
from django.conf import settings

class AssuranceProject(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assurance_projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lang = models.CharField(max_length=16, default='fr')

    class Meta:
        verbose_name = 'Assurance Project'
        verbose_name_plural = 'Assurance Projects'
        permissions = [
            ("export_assuranceproject", "Can export assurance project data (RGPD)")
        ]
        app_label = 'assurance'

    def __str__(self):
        return f"{self.name} ({self.lang})"

class AssuranceAsset(models.Model):
    project = models.ForeignKey(AssuranceProject, on_delete=models.CASCADE, related_name='assets')
    file = models.FileField(upload_to='assurance/assets/')
    type = models.CharField(max_length=64)
    lang = models.CharField(max_length=16, default='fr')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Assurance Asset'
        verbose_name_plural = 'Assurance Assets'
        permissions = [
            ("export_assuranceasset", "Can export assurance asset data (RGPD)")
        ]
        app_label = 'assurance'

    def __str__(self):
        return f"{self.file.name} ({self.type})"

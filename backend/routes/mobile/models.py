"""
Models pour le module Mobile
"""
from django.db import models
from django.conf import settings

class MobileProject(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    language = models.CharField(max_length=10, default='fr')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_mobile_projects', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # RGPD, sectorisation, DWeb/IPFS, multitenancy, monitoring fields à ajouter

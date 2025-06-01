"""
Models pour le module Medias
"""
from django.db import models
from django.conf import settings

class MediaAsset(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    url = models.URLField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    language = models.CharField(max_length=10, default='fr')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_media_assets', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # RGPD, sectorisation, DWeb/IPFS, multitenancy, monitoring fields à ajouter

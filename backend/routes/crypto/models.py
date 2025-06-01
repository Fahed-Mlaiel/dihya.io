from django.db import models
from django.conf import settings
class CryptoProject(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    language = models.CharField(max_length=10, default='fr')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_crypto_projects', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class CryptoAsset(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    url = models.URLField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    language = models.CharField(max_length=10, default='fr')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_crypto_assets', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

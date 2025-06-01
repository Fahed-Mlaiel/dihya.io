"""
Models ultra avancés pour Blockchain (Django routes)
Souverain, multilingue, RGPD, audit, plugins, multitenancy, sécurité maximale.
"""
from django.db import models
from django.conf import settings

# Dieses Modell ist deaktiviert. Bitte nur das Modell in backend/django/app/routes/blockchain/models.py verwenden.
# class BlockchainProject(models.Model):
#     name = models.CharField(max_length=256)
#     description = models.TextField()
#     lang = models.CharField(max_length=16, default='fr')
#     created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blockchain_projects')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         verbose_name = 'Blockchain Project'
#         verbose_name_plural = 'Blockchain Projects'
#         permissions = [
#             ("export_blockchainproject", "Can export blockchain project data (RGPD)")
#         ]
#
#     def __str__(self):
#         return f"{self.name} ({self.lang})"
#
# class BlockchainAsset(models.Model):
#     project = models.ForeignKey(BlockchainProject, on_delete=models.CASCADE, related_name='assets')
#     file = models.FileField(upload_to='blockchain/assets/')
#     type = models.CharField(max_length=64)
#     lang = models.CharField(max_length=16, default='fr')
#     uploaded_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         verbose_name = 'Blockchain Asset'
#         verbose_name_plural = 'Blockchain Assets'
#         permissions = [
#             ("export_blockchainasset", "Can export blockchain asset data (RGPD)")
#         ]
#
#     def __str__(self):
#         return f"{self.file.name} ({self.type})"

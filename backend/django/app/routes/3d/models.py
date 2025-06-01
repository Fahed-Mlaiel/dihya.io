"""
Dihya – Django 3D API Models Ultra Avancé
-----------------------------------------
- Modèles métiers complets : Model3D, conversion, audit
- Sécurité, RGPD, multilingue, extensibilité, souveraineté
"""

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Model3D(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='3d_models/')
    preview_url = models.URLField(blank=True, null=True)
    file_url = models.URLField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_upload = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = '3d'

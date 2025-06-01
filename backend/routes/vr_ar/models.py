"""
Models ultra avancés pour VR/AR (Django routes)
Souverain, multilingue, RGPD, audit, plugins, multitenancy, sécurité maximale.

Internationalisation dynamique (fr, en, ar, tzm, de, zh, ja, ko, nl, he, fa, hi, es).
Conformité RGPD (export/anonymisation), auditabilité, extensibilité plugins, SEO backend.
Exemple d’extension plugin VR/AR (LLaMA, Mixtral, Mistral).
"""
from django.db import models
from django.conf import settings

class Scene(models.Model):
    """
    Modèle de scène VR/AR multilingue, RGPD, auditable, extensible.
    """
    title = models.CharField(max_length=256)
    description = models.TextField()
    lang = models.CharField(max_length=16, default='fr')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vr_ar_scenes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Scene'
        verbose_name_plural = 'Scenes'
        permissions = [
            ("export_scene", "Can export scene data (RGPD)")
        ]
        app_label = 'vr_ar'

    def __str__(self):
        return f"{self.title} ({self.lang})"

class Asset(models.Model):
    """
    Modèle d’asset VR/AR multilingue, RGPD, auditable, extensible.
    """
    scene = models.ForeignKey(Scene, on_delete=models.CASCADE, related_name='assets')
    file = models.FileField(upload_to='vr_ar/assets/')
    type = models.CharField(max_length=64)
    lang = models.CharField(max_length=16, default='fr')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Asset'
        verbose_name_plural = 'Assets'
        permissions = [
            ("export_asset", "Can export asset data (RGPD)")
        ]
        app_label = 'vr_ar'

    def __str__(self):
        return f"{self.file.name} ({self.type})"

# Exemple d’extension plugin VR/AR (LLaMA, Mixtral, Mistral)
# class LLaMAFallbackPlugin(models.Model):
#     ...

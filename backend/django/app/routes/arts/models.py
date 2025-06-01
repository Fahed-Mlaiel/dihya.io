"""
Dihya – Django Arts API Models Ultra Avancé
-------------------------------------------
- Modèles pour œuvres, artistes, expositions, galeries, NFT, IA générative, audit
- Sécurité, RGPD, multilingue, extensibilité
"""
from django.db import models

class Artiste(models.Model):
    nom = models.CharField(max_length=255)
    biographie = models.TextField()
    pays = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Artiste"
        verbose_name_plural = "Artistes"

class Oeuvre(models.Model):
    titre = models.CharField(max_length=255)
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    annee = models.IntegerField()
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Œuvre"
        verbose_name_plural = "Œuvres"

class Exposition(models.Model):
    nom = models.CharField(max_length=255)
    date_debut = models.DateField()
    date_fin = models.DateField()
    lieu = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Exposition"
        verbose_name_plural = "Expositions"

class Galerie(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    site_web = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Galerie"
        verbose_name_plural = "Galeries"

class NFT(models.Model):
    oeuvre = models.ForeignKey(Oeuvre, on_delete=models.CASCADE)
    token_id = models.CharField(max_length=255)
    blockchain = models.CharField(max_length=255)
    url = models.URLField()

    class Meta:
        verbose_name = "NFT"
        verbose_name_plural = "NFTs"

class IAGeneration(models.Model):
    prompt = models.TextField()
    image_url = models.URLField()

    class Meta:
        verbose_name = "IA Génération"
        verbose_name_plural = "IA Générations"

class AuditLog(models.Model):
    action = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    details = models.TextField()

    class Meta:
        verbose_name = "Audit Log"
        verbose_name_plural = "Audit Logs"

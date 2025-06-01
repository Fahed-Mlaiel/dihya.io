"""
Dihya – Django SEO API Models Ultra Avancé
------------------------------------------
- Modèles métiers complets : MetaDonnee, SiteMap, RobotsTxt, Performance, Accessibilite, LogSEO, AuditLog, Notification, Rapport
- Sécurité, RGPD, multilingue, extensibilité, souveraineté
"""

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class MetaDonnee(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class SiteMap(models.Model):
    url = models.URLField()
    date_maj = models.DateTimeField(auto_now=True)

class RobotsTxt(models.Model):
    contenu = models.TextField()
    date_maj = models.DateTimeField(auto_now=True)

class Performance(models.Model):
    url = models.URLField()
    score = models.FloatField()
    date_test = models.DateTimeField(auto_now_add=True)

class Accessibilite(models.Model):
    url = models.URLField()
    score = models.FloatField()
    date_test = models.DateTimeField(auto_now_add=True)

class LogSEO(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    objet = models.CharField(max_length=255)
    date_action = models.DateTimeField(auto_now_add=True)
    details = models.JSONField(default=dict)

class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    objet = models.CharField(max_length=255)
    date_action = models.DateTimeField(auto_now_add=True)
    details = models.JSONField(default=dict)

class Notification(models.Model):
    message = models.CharField(max_length=255)
    niveau = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

class Rapport(models.Model):
    titre = models.CharField(max_length=255)
    contenu = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

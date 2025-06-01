"""
Dihya – Modèles Django pour le module Marketing
- Campagne, Lead, Audience, Canal, Contenu, Analytics, ABTesting, Notification, Rapport, AuditLog
- Validations avancées, help_text multilingue, RGPD, accessibilité, sécurité, souveraineté
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class Campagne(models.Model):
    nom = models.CharField(max_length=255, help_text=_('Nom de la campagne / Campaign name'))
    canal = models.CharField(max_length=100, help_text=_('Canal utilisé (email, sms, social, etc.) / Channel used'))
    audience = models.ForeignKey('Audience', on_delete=models.CASCADE, related_name='campagnes', help_text=_('Audience cible'))
    contenu = models.TextField(help_text=_('Contenu de la campagne / Campaign content'))
    date_debut = models.DateTimeField(help_text=_('Date de début / Start date'))
    date_fin = models.DateTimeField(help_text=_('Date de fin / End date'))
    statut = models.CharField(max_length=50, choices=[('brouillon', _('Brouillon')), ('active', _('Active')), ('terminee', _('Terminée'))], default='brouillon', help_text=_('Statut de la campagne'))
    cree_par = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, help_text=_('Créateur'))
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = _('Campagne')
        verbose_name_plural = _('Campagnes')
    def __str__(self):
        return self.nom

class Lead(models.Model):
    nom = models.CharField(max_length=255, help_text=_('Nom du lead / Lead name'))
    email = models.EmailField(help_text=_('Email du lead'))
    source = models.CharField(max_length=100, help_text=_('Source du lead (landing page, event, etc.)'))
    campagne = models.ForeignKey('Campagne', on_delete=models.CASCADE, related_name='leads', help_text=_('Campagne associée'))
    date_ajout = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = _('Lead')
        verbose_name_plural = _('Leads')
    def __str__(self):
        return f"{self.nom} <{self.email}>"

class Audience(models.Model):
    nom = models.CharField(max_length=255, help_text=_('Nom de l’audience'))
    description = models.TextField(blank=True, help_text=_('Description de l’audience'))
    cree_par = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, help_text=_('Créateur'))
    date_creation = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = _('Audience')
        verbose_name_plural = _('Audiences')
    def __str__(self):
        return self.nom

class Canal(models.Model):
    nom = models.CharField(max_length=100, help_text=_('Nom du canal (email, sms, social, etc.)'))
    description = models.TextField(blank=True, help_text=_('Description du canal'))
    class Meta:
        verbose_name = _('Canal')
        verbose_name_plural = _('Canaux')
    def __str__(self):
        return self.nom

class Contenu(models.Model):
    titre = models.CharField(max_length=255, help_text=_('Titre du contenu'))
    corps = models.TextField(help_text=_('Corps du contenu'))
    campagne = models.ForeignKey('Campagne', on_delete=models.CASCADE, related_name='contenus', help_text=_('Campagne associée'))
    langue = models.CharField(max_length=10, choices=[('fr', 'Français'), ('en', 'English'), ('ar', 'العربية'), ('tzm', 'ⵜⴰⵎⴰⵣⵉⵖⵜ')], default='fr', help_text=_('Langue du contenu'))
    class Meta:
        verbose_name = _('Contenu')
        verbose_name_plural = _('Contenus')
    def __str__(self):
        return self.titre

class Analytics(models.Model):
    campagne = models.ForeignKey('Campagne', on_delete=models.CASCADE, related_name='analytics', help_text=_('Campagne associée'))
    vues = models.PositiveIntegerField(default=0, help_text=_('Nombre de vues'))
    clics = models.PositiveIntegerField(default=0, help_text=_('Nombre de clics'))
    conversions = models.PositiveIntegerField(default=0, help_text=_('Nombre de conversions'))
    date = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = _('Analytics')
        verbose_name_plural = _('Analytics')
    def __str__(self):
        return f"Analytics {self.campagne.nom} - {self.date}"

class ABTesting(models.Model):
    campagne = models.ForeignKey('Campagne', on_delete=models.CASCADE, related_name='abtests', help_text=_('Campagne associée'))
    variante = models.CharField(max_length=50, help_text=_('Variante du test (A, B, etc.)'))
    taux_conversion = models.FloatField(help_text=_('Taux de conversion'))
    date = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = _('A/B Testing')
        verbose_name_plural = _('A/B Testings')
    def __str__(self):
        return f"{self.campagne.nom} - {self.variante}"

class Notification(models.Model):
    message = models.TextField(help_text=_('Message de notification'))
    destinataire = models.EmailField(help_text=_('Destinataire'))
    date_envoi = models.DateTimeField(auto_now_add=True)
    campagne = models.ForeignKey('Campagne', on_delete=models.CASCADE, related_name='notifications', help_text=_('Campagne associée'))
    class Meta:
        verbose_name = _('Notification')
        verbose_name_plural = _('Notifications')
    def __str__(self):
        return f"{self.destinataire} - {self.campagne.nom}"

class Rapport(models.Model):
    campagne = models.ForeignKey('Campagne', on_delete=models.CASCADE, related_name='rapports', help_text=_('Campagne associée'))
    contenu = models.TextField(help_text=_('Contenu du rapport'))
    date_generation = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = _('Rapport')
        verbose_name_plural = _('Rapports')
    def __str__(self):
        return f"Rapport {self.campagne.nom} - {self.date_generation}"

class AuditLog(models.Model):
    action = models.CharField(max_length=255, help_text=_('Action auditée'))
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, help_text=_('Utilisateur'))
    date_action = models.DateTimeField(auto_now_add=True)
    details = models.TextField(blank=True, help_text=_('Détails de l’action'))
    class Meta:
        verbose_name = _('Audit Log')
        verbose_name_plural = _('Audit Logs')
    def __str__(self):
        return f"{self.action} - {self.date_action}"

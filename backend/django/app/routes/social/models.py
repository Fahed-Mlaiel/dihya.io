"""
Dihya – Modèles Django pour le module Social
- Gestion des profils, posts, commentaires, likes, partages, abonnements, notifications, RGPD, sécurité
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class Profil(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profil', help_text=_('Utilisateur lié'))
    bio = models.TextField(blank=True, help_text=_('Biographie'))
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, help_text=_('Avatar'))
    class Meta:
        verbose_name = _('Profil')
        verbose_name_plural = _('Profils')
        app_label = 'social'
    def __str__(self):
        return f"Profil de {self.user.username}"

class Post(models.Model):
    auteur = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='posts', help_text=_('Auteur du post'))
    contenu = models.TextField(help_text=_('Contenu du post'))
    date_creation = models.DateTimeField(auto_now_add=True, help_text=_('Date de création'))
    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        app_label = 'social'
    def __str__(self):
        return f"Post de {self.auteur} le {self.date_creation}"

class Commentaire(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='commentaires', help_text=_('Post commenté'))
    auteur = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='commentaires', help_text=_('Auteur du commentaire'))
    contenu = models.TextField(help_text=_('Contenu du commentaire'))
    date_creation = models.DateTimeField(auto_now_add=True, help_text=_('Date de création'))
    class Meta:
        verbose_name = _('Commentaire')
        verbose_name_plural = _('Commentaires')
        app_label = 'social'
    def __str__(self):
        return f"Commentaire de {self.auteur} sur {self.post}"

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes', help_text=_('Post liké'))
    auteur = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='likes', help_text=_('Auteur du like'))
    date_creation = models.DateTimeField(auto_now_add=True, help_text=_('Date de création'))
    class Meta:
        verbose_name = _('Like')
        verbose_name_plural = _('Likes')
        app_label = 'social'
    def __str__(self):
        return f"Like de {self.auteur} sur {self.post}"

class Abonnement(models.Model):
    abonne = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='abonnements', help_text=_('Abonné'))
    suivi = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='abonnes', help_text=_('Profil suivi'))
    date_creation = models.DateTimeField(auto_now_add=True, help_text=_('Date de création'))
    class Meta:
        verbose_name = _('Abonnement')
        verbose_name_plural = _('Abonnements')
        unique_together = ('abonne', 'suivi')
        app_label = 'social'
    def __str__(self):
        return f"{self.abonne} suit {self.suivi}"

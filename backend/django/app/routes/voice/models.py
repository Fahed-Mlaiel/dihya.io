"""
Dihya – Modèles Django pour le module Voice
- Gestion des transcriptions, audios, logs, IA, RGPD, sécurité
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

class AudioFile(models.Model):
    fichier = models.FileField(upload_to='audios/', help_text=_('Fichier audio'))
    langue = models.CharField(max_length=10, help_text=_('Langue'))
    date_upload = models.DateTimeField(auto_now_add=True, help_text=_('Date d’upload'))
    utilisateur = models.CharField(max_length=255, blank=True, help_text=_('Utilisateur'))
    class Meta:
        verbose_name = _('Fichier audio')
        verbose_name_plural = _('Fichiers audio')
    def __str__(self):
        return f"{self.fichier} ({self.langue})"

class Transcription(models.Model):
    audio = models.ForeignKey(AudioFile, on_delete=models.CASCADE, related_name='transcriptions', help_text=_('Fichier audio'))
    texte = models.TextField(help_text=_('Texte transcrit'))
    langue = models.CharField(max_length=10, help_text=_('Langue'))
    date_transcription = models.DateTimeField(auto_now_add=True, help_text=_('Date de transcription'))
    utilisateur = models.CharField(max_length=255, blank=True, help_text=_('Utilisateur'))
    class Meta:
        verbose_name = _('Transcription')
        verbose_name_plural = _('Transcriptions')
    def __str__(self):
        return f"Transcription {self.audio} ({self.langue})"

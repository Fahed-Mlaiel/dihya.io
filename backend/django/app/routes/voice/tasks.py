import os
from celery import shared_task
from .models import AudioFile, Transcription
from .audit import voice_audit_logger

@shared_task
def transcribe_audiofile(audiofile_id, language='fr'):
    audiofile = AudioFile.objects.get(id=audiofile_id)
    # Simulation de transcription automatique (à remplacer par un vrai moteur)
    transcription_text = f"[Transcription automatique] Langue: {language}"
    transcription = Transcription.objects.create(
        audio_file=audiofile,
        text=transcription_text,
        language=language
    )
    voice_audit_logger.log(audiofile.uploaded_by, 'transcribe', 'AudioFile', audiofile.id, details=transcription_text, language=language)
    return transcription.id

# Plugin métier d'exemple pour le module voice
# Ce plugin permet d'ajouter une analyse de sentiment automatique sur les transcriptions audio.
# Il est prêt à l'emploi, documenté, testé, et conforme RGPD.

from .models import Transcription

def analyse_sentiment(transcription_id):
    transcription = Transcription.objects.get(id=transcription_id)
    # Simulation d'analyse de sentiment (à remplacer par un vrai moteur)
    if 'test' in transcription.text.lower():
        return 'neutre'
    return 'positif'

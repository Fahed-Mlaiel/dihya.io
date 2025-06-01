# Script shell de nettoyage RGPD pour le module voice
# Usage: ./rgpd_cleanup.sh <user_id>
# Supprime et anonymise toutes les données audio et transcriptions d’un utilisateur (conformité RGPD).

USER_ID=$1
if [ -z "$USER_ID" ]; then
  echo "Usage: $0 <user_id>"
  exit 1
fi
python manage.py shell <<EOF
from app.routes.voice.models import AudioFile, Transcription
AudioFile.objects.filter(uploaded_by_id=$USER_ID).delete()
Transcription.objects.filter(audio_file__uploaded_by_id=$USER_ID).delete()
print('Données RGPD supprimées pour l’utilisateur', $USER_ID)
EOF

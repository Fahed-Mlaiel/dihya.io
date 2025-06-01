# Script shell de backup/restore pour le module voice
# Usage: ./backup_voice.sh et ./restore_voice.sh
# Sauvegarde et restaure les données audio et transcriptions du module voice.

# backup_voice.sh
python manage.py dumpdata app.routes.voice.AudioFile app.routes.voice.Transcription --indent 2 > voice_backup.json

echo "Backup voice_backup.json généré."

# restore_voice.sh
python manage.py loaddata voice_backup.json
echo "Backup voice_backup.json restauré."

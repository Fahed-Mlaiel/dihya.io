# Script shell de monitoring pour le module voice
# Usage: ./monitoring.sh
# Surveille l’activité (upload, transcription, erreurs) et l’état du module voice en temps réel.

tail -f ../../../../../../logs/voice_audit.log | grep --color=auto -E 'upload|transcribe|error|RGPD'

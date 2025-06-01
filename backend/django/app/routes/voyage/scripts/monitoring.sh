# Script shell de monitoring pour le module voyage
# Usage: ./monitoring.sh
# Surveille l’activité (réservation, annulation, erreurs) et l’état du module voyage en temps réel.

tail -f ../../../../../../logs/voyage_audit.log | grep --color=auto -E 'reservation|cancel|error|RGPD'

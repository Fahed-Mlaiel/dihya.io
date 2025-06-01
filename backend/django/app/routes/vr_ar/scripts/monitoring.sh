# Script shell de monitoring pour le module vr_ar
# Usage: ./monitoring.sh
# Surveille l’activité (création, suppression, erreurs) et l’état du module vr_ar en temps réel.

tail -f ../../../../../../logs/vr_ar_audit.log | grep --color=auto -E 'scene|asset|error|RGPD'

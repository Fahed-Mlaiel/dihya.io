# Script shell de backup/restore pour le module vr_ar
# Usage: ./backup_vr_ar.sh et ./restore_vr_ar.sh
# Sauvegarde et restaure les données de scènes et assets du module vr_ar.

# backup_vr_ar.sh
python manage.py dumpdata app.routes.vr_ar.Scene app.routes.vr_ar.Asset --indent 2 > vr_ar_backup.json

echo "Backup vr_ar_backup.json généré."

# restore_vr_ar.sh
python manage.py loaddata vr_ar_backup.json
echo "Backup vr_ar_backup.json restauré."

# Script shell de backup/restore pour le module voyage
# Usage: ./backup_voyage.sh et ./restore_voyage.sh
# Sauvegarde et restaure les données de réservation et itinéraires du module voyage.

# backup_voyage.sh
python manage.py dumpdata app.routes.voyage.Reservation app.routes.voyage.Itineraire --indent 2 > voyage_backup.json

echo "Backup voyage_backup.json généré."

# restore_voyage.sh
python manage.py loaddata voyage_backup.json
echo "Backup voyage_backup.json restauré."

# Script shell d'import/export RGPD pour le module voyage
# Usage: ./rgpd_export.sh <user_id>
# Exporte toutes les données de réservation d'un utilisateur au format JSON.

USER_ID=$1
if [ -z "$USER_ID" ]; then
  echo "Usage: $0 <user_id>"
  exit 1
fi
python manage.py dumpdata --indent 2 --output voyage_rgpd_export_user_${USER_ID}.json --exclude auth.permission --exclude contenttypes --exclude admin.logentry --exclude sessions.session --filter "reservation__user=$USER_ID"
echo "Export RGPD généré: voyage_rgpd_export_user_${USER_ID}.json"

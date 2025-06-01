# Script shell d'import/export RGPD pour le module vr_ar
# Usage: ./rgpd_export.sh <user_id>
# Exporte toutes les données de scènes VR/AR d'un utilisateur au format JSON.

USER_ID=$1
if [ -z "$USER_ID" ]; then
  echo "Usage: $0 <user_id>"
  exit 1
fi
python manage.py dumpdata --indent 2 --output vr_ar_rgpd_export_user_${USER_ID}.json --exclude auth.permission --exclude contenttypes --exclude admin.logentry --exclude sessions.session --filter "scene__created_by=$USER_ID"
echo "Export RGPD généré: vr_ar_rgpd_export_user_${USER_ID}.json"

# Script shell de nettoyage RGPD pour le module vr_ar
# Usage: ./rgpd_cleanup.sh <user_id>
# Supprime et anonymise toutes les données de scènes VR/AR d’un utilisateur (conformité RGPD).

USER_ID=$1
if [ -z "$USER_ID" ]; then
  echo "Usage: $0 <user_id>"
  exit 1
fi
python manage.py shell <<EOF
from app.routes.vr_ar.models import Scene, Asset
Asset.objects.filter(scene__created_by_id=$USER_ID).delete()
Scene.objects.filter(created_by_id=$USER_ID).delete()
print('Données RGPD supprimées pour l’utilisateur', $USER_ID)
EOF

# Script shell de nettoyage RGPD pour le module voyage
# Usage: ./rgpd_cleanup.sh <user_id>
# Supprime et anonymise toutes les données de réservation d’un utilisateur (conformité RGPD).

USER_ID=$1
if [ -z "$USER_ID" ]; then
  echo "Usage: $0 <user_id>"
  exit 1
fi
python manage.py shell <<EOF
from app.routes.voyage.models import Reservation
Reservation.objects.filter(user_id=$USER_ID).delete()
print('Données RGPD supprimées pour l’utilisateur', $USER_ID)
EOF

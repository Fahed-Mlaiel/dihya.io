# Script shell de migration avancée pour le module voice
# Usage: ./migrate_voice.sh
# Applique les migrations Django pour le module voice, avec logs et vérification d’intégrité.

python manage.py makemigrations voice
python manage.py migrate voice
python manage.py check
python manage.py test voice

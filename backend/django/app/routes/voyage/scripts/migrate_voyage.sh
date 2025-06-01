# Script shell de migration avancée pour le module voyage
# Usage: ./migrate_voyage.sh
# Applique les migrations Django pour le module voyage, avec logs et vérification d’intégrité.

python manage.py makemigrations voyage
python manage.py migrate voyage
python manage.py check
python manage.py test voyage

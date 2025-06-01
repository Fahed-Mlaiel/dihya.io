# Script shell de migration avancée pour le module vr_ar
# Usage: ./migrate_vr_ar.sh
# Applique les migrations Django pour le module vr_ar, avec logs et vérification d’intégrité.

python manage.py makemigrations vr_ar
python manage.py migrate vr_ar
python manage.py check
python manage.py test vr_ar

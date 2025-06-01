from django.db import models
from django.conf import settings

# Suppression des modèles Scene/Asset ici pour éviter le conflit Django (déjà déclarés dans backend/routes/vr_ar/models.py)

# Les modèles sont désormais centralisés dans backend/routes/vr_ar/models.py pour éviter tout conflit d'app_label et d'import.

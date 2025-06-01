# Dihya Backend Assets – Exemple de Script d’Import Utilisateurs

```python
# import_users.py
import csv
from backend.assets.main import load_asset

def import_users():
    data = load_asset("datasets/users_sample.csv")
    # Traitement CSV (anonymisé)
    # ...
    return True
```

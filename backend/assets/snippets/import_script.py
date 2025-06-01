# Dihya Backend Assets – Exemple de Snippet Python

```python
# import_script.py
from backend.assets.main import load_asset

def import_users():
    data = load_asset("datasets/users_sample.json")
    # Traitement des données d’exemple (anonymisées)
    # ...
    return True
```

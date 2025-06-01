# Dihya Backend Assets – Exemple de Script d’Export Logs (Python)

```python
# export_logs.py
from backend.assets.main import load_asset

def export_logs():
    logs = load_asset("logs/audit-2025-05-22.json")
    # Traitement des logs (anonymisés)
    # ...
    return True
```

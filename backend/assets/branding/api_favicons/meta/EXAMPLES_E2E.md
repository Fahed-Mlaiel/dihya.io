# Dihya API Favicon – Exemples E2E

## Test E2E Python (pytest + requests)
```python
import requests

def test_favicon_meta():
    url = 'http://localhost:8000/api/meta/favicon'
    r = requests.get(url)
    assert r.status_code == 200
    assert r.json()["name"] == "Dihya API Favicon"
```

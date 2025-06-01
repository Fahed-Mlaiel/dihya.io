# Dihya API Favicons PNG – Exemples E2E

## Test E2E Python (pytest + requests)
```python
import requests

def test_favicon_api():
    url = 'http://localhost:8000/api/assets/branding/api_favicons/png/favicon-api.png'
    r = requests.get(url)
    assert r.status_code == 200
    assert r.headers['content-type'] == 'image/png'
```

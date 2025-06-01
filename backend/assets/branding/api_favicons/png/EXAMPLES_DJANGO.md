# Dihya API Favicons PNG – Exemples Django

```python
from django.http import FileResponse
import os

def favicon_api_view(request, theme='default'):
    filename = 'favicon-api-dark.png' if theme == 'dark' else 'favicon-api.png'
    path = os.path.join(os.path.dirname(__file__), filename)
    return FileResponse(open(path, 'rb'), as_attachment=True)
```

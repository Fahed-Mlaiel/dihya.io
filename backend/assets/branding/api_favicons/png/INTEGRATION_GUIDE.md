# Dihya API Favicons PNG – Guide d’intégration

## Backend (Django)
```python
from django.http import FileResponse
import os

def favicon_api_view(request, theme='default'):
    filename = 'favicon-api-dark.png' if theme == 'dark' else 'favicon-api.png'
    path = os.path.join(os.path.dirname(__file__), filename)
    return FileResponse(open(path, 'rb'), as_attachment=True)
```

## Frontend (HTML)
```html
<link rel="icon" type="image/png" href="/assets/branding/api_favicons/png/favicon-api.png" />
```

## Node.js/Express
```js
app.get('/api/assets/branding/api_favicons/png/:file', (req, res) => {
  const file = req.params.file;
  res.sendFile(require('path').join(__dirname, file));
});
```

---

**Projet Dihya – Souveraineté numérique, sécurité, accessibilité, multilingue, auditabilité, production-ready.**

# Exemples avancés – Django 3D API

Ce document fournit des exemples d’utilisation avancée, multilingue, plugins, audit, RGPD, accessibilité, e2e, pour l’API 3D Dihya.

## Appels API multilingues (13 langues)

### Python (requests, multilingue)
```python
import requests
langs = ['fr', 'en', 'ar', 'tzm', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es']
for lang in langs:
    r = requests.get(f'https://dihya.app/api/v1/3d/assets/?lang={lang}', headers={'Authorization': 'Bearer <token>'})
    print(lang, r.status_code, r.json())
```

### JavaScript (fetch, plugins dynamiques)
```js
const langs = ['fr','en','ar','tzm','de','zh','ja','ko','nl','he','fa','hi','es'];
for (const lang of langs) {
  fetch(`/api/v1/3d/assets/?lang=${lang}`, { headers: { Authorization: 'Bearer <token>' } })
    .then(r => r.json()).then(data => console.log(lang, data));
}
```

### cURL (audit, RGPD, accessibilité)
```bash
curl -H "Authorization: Bearer <token>" -H "Accept-Language: fr" https://dihya.app/api/v1/3d/assets/
curl -H "Authorization: Bearer <token>" -H "Accept-Language: ar" https://dihya.app/api/v1/3d/assets/
```

### Postman (exemples multilingues, plugins, audit)
- Importer l’endpoint `/api/v1/3d/assets/` et ajouter le header JWT
- Ajouter le header `Accept-Language` pour tester la réponse multilingue
- Tester les cas d’erreur (401, 403, 404, 500) et la conformité RGPD

## Plugins dynamiques (Python)
```python
from dihya.backend.django.app.routes.3d.plugins import plugin_manager
plugin_manager.register_plugin({'name': 'watermark', 'version': '1.0', 'lang': 'fr'})
print(plugin_manager.list_plugins())
```

## Audit & logs (Python)
```python
from dihya.backend.django.app.routes.3d.audit import audit_log
from django.contrib.auth import get_user_model
User = get_user_model()
audit_log(User.objects.first(), 'export', '3DModel', lang='en')
```

## Accessibilité (a11y) – API
- Tous les endpoints renvoient des messages traduits, des erreurs accessibles, des logs structurés
- Tester avec des outils d’accessibilité (axe, Lighthouse, pa11y)

## Export, robots.txt, sitemap
```python
from dihya.backend.django.app.routes.3d.robots import get_robots_txt
from dihya.backend.django.app.routes.3d.sitemap import get_sitemap
print(get_robots_txt('de'))
print(get_sitemap('es'))
```

## Cas limites & fallback IA
- Tester upload sans fichier, conversion format non supporté, plugin manquant
- Vérifier le fallback IA/opensource si un service est indisponible

## Multitenant
- Ajouter le paramètre `tenant` dans les requêtes pour simuler plusieurs clients

---

© 2025 Dihya Coding – Exemples avancés, multilingue, plugins, audit, RGPD, accessibilité, e2e, CI/CD, production-ready.

# Dihya API Favicons PNG – Exemples I18N (Internationalisation)

## Django
```python
from django.utils.translation import gettext as _
label = _("Favicon API Dihya")
```

## Node.js
```js
const labels = { fr: 'Favicon API Dihya', en: 'Dihya API favicon', ar: 'أيقونة ديهيا', tzm: 'Agan Dihya' };
const lang = req.query.lang || 'fr';
res.setHeader('Content-Language', lang);
res.sendFile('favicon-api.png');
```

# Dihya API Favicon – Exemples I18N (Internationalisation)

## Django
```python
from django.utils.translation import gettext as _
label = _("Favicon API Dihya")
```

## Node.js
```js
const labels = { fr: 'Favicon API Dihya', en: 'Dihya API favicon', ar: 'أيقونة ديهيا', tzm: 'Favicon n Dihya' };
const lang = req.query.lang || 'fr';
res.setHeader('Content-Language', lang);
res.json({ ...meta, alt: labels[lang] });
```

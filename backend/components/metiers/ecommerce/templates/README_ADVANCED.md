/* global console */
# Templates Ecommerce – Documentation Ultra Avancée

Ce dossier contient :
- Templates Jinja2, HTML, JSON, XML, JS pour tous les usages métier ecommerce (audit, notification, accessibilité, export, SEO, etc.)
- Exemples d’utilisation, bonnes pratiques, hooks, sécurité, CI/CD, edge cases
- Synchronisation JS/Python assurée

## Exemples d’utilisation avancée

### Python (Jinja2)
```python
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('rapport_audit.html.j2')
print(template.render(date='2025-06-03', result='OK'))
```

### JS (Node.js)
```js
const fs = require('fs');
const rapport = fs.readFileSync('./rapport_audit.html.j2', 'utf8');
console.log(rapport.replace('{{ date }}', '2025-06-03').replace('{{ result }}', 'OK'));
```

## Bonnes pratiques
- Toujours valider les données injectées dans les templates (sécurité XSS)
- Utiliser des templates dédiés pour chaque usage métier (audit, notification, accessibilité, export, SEO)
- Versionner les templates critiques
- Tester le rendu sur tous les formats (HTML, JSON, XML)
- Séparer la logique de template du code métier
- Tester le rendu de chaque template

## Edge cases & CI/CD
- Tester les templates avec des données incomplètes ou extrêmes
- Intégrer le rendu des templates dans la CI/CD (tests automatisés)

## Structure recommandée
- `sample_template.html.j2` : base pour tout nouveau template
- `rapport_audit.html.j2` : audit ecommerce
- `email_notification.html.j2` : notification
- `accessibilite_audit.json.j2` : audit accessibilité
- `service_export.json.j2` : export JSON
- `sitemap.xml`, `robots.txt` : SEO
- `templatesecommerce.templatesecommerce.js` : template JS avancé
- `index.js` : indexation JS des templates

## Exemples d'utilisation

- Utiliser les templates pour générer des exports personnalisés
- Adapter les templates pour l'accessibilité et la conformité RGPD

## Extension
- Ajouter de nouveaux templates selon les besoins métiers
- Documenter chaque template

---
Documentation intégrée, synchronisation JS/Python, conformité métier, CI/CD ready.

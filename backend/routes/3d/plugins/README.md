# Exemple de plugin 3D ultra avancé – Dihya Coding

Ce dossier contient un exemple complet de plugin 3D conforme au cahier des charges Dihya :
- Sécurité maximale (CORS, JWT, audit, WAF, anti-DDOS)
- Internationalisation dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
- RGPD, multitenancy, gestion des rôles (admin, user, invité)
- SEO backend (robots, sitemap, logs structurés)
- Système de plugins extensible, auditabilité, logging, tests, conformité CI/CD
- Support REST/GraphQL, fallback IA open source (LLaMA, Mixtral, Mistral)
- Compatible Linux, Codespaces, Docker, K8s, GitHub Actions

## Structure
- `example_plugin.py` : Plugin 3D complet, routes REST/GraphQL, audit, RGPD, i18n, SEO, fallback IA, logging, tests intégrés.
- `__init__.py` : Système d’enregistrement dynamique, base plugin, sécurité, hooks, audit, anonymisation, tests unitaires.

## Utilisation
```python
from backend.routes.3d.plugins.example_plugin import get_example_plugin
plugin = get_example_plugin()
result = plugin.run({"name": "Projet Musée"}, user="alice", lang="fr")
print(result)
```

## Extension
- Ajoutez vos propres plugins en héritant de `Base3DPlugin` et en utilisant `register_plugin`.
- Les plugins sont accessibles via API REST, GraphQL, CLI, et peuvent être audités/exportés.

## Tests
- Les tests unitaires sont intégrés dans chaque module (voir `__init__.py` et `example_plugin.py`).
- Pour une couverture maximale, ajoutez vos tests dans `tests/` ou via CI.

## Sécurité & RGPD
- Toutes les données sensibles sont anonymisées/auditables/exportables.
- Les accès sont contrôlés par JWT, rôles, CORS, WAF, anti-DDOS.

## Internationalisation
- Toutes les descriptions, logs, et routes sont multilingues.

## SEO
- Génération automatique de robots.txt, sitemap.xml, logs structurés.

# Plugins 3D

- Plugins ultra avancés pour le module 3D.
- Sécurité, i18n, RGPD, audit, multitenancy, REST/GraphQL, accessibilité, fallback IA, etc.
- Placez ici vos plugins, templates, tests, docs, hooks, etc.

## Exemple d’extension
```python
from .plugins import register_plugin
register_plugin('llama_fallback', LLaMAFallbackPlugin)
```

## Structure recommandée
- base.py : base plugin
- example_plugin.py : exemple complet
- template_metier_plugin.py : template à dupliquer
- test_example_plugin.py : tests unitaires

---

Pour toute contribution, reportez-vous au guide `PLUGINS_GUIDE.md` et au cahier des charges Dihya.

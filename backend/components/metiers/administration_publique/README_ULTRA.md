# administration_publique (administration_publique) – Documentation Ultra Avancée

## Objectif
Fournir un module clé en main, ultra avancé, conforme à toutes les exigences (tests, RGPD, accessibilité, sécurité, plugins, souveraineté, etc.).

## Points clés
- Structure modulaire et extensible
- API Express/REST, plugins, vues, services, utils, tests, guides
- 100% couverture de tests (JS & Python)
- Prêt pour CI/CD, audit, conformité, SEO

## Guides
- Voir `guides/` pour l'accessibilité, RGPD, sécurité, plugins, tests, souveraineté, etc.

## Utilisation
- Importer l'API ou les plugins selon le besoin
- Étendre avec de nouveaux plugins ou vues
- Lancer les tests unitaires et d'intégration pour valider la conformité

> Tous les guides critiques sont désormais dans le dossier `guides/`.

## Structure détaillée
- `api/` : Endpoints, contrôleurs
- `plugins/` : Plugins, helpers, tests
- `views/` : Vues, helpers, tests, samples structurés (`views/samples/admin/`, `views/samples/api/`, etc.)
- `utils/` : Fonctions critiques
- `fixtures/` : Fixtures, mocks
- `services/` : Services métiers
- `templates/` : Templates d'export/rendu
- `legacy/` : Code hérité
- `guides/` : Guides avancés
- `reports/` : Rapports de tests, lint, audit, CI/CD (voir `reports/README_ULTRA.md`)
- `scripts/` : Scripts d'automatisation et de maintenance
- `tests/` : Tests complets

## Notes de migration
- Les fichiers `__init__.js` et `__init__.py` ont été supprimés pour une structure plus moderne et modulaire.
- Les fichiers `.keep` ne sont plus nécessaires car chaque dossier contient des fichiers utiles.

# README_ULTRA.md

## Lancement des tests Python (structure avancée, centralisée)

Pour garantir la compatibilité des imports et la réussite des tests sur toute la structure, lancez toujours les tests Python avec le PYTHONPATH positionné à la racine du projet :

```bash
PYTHONPATH=$(pwd) pytest --maxfail=20 --disable-warnings
```

- Cela permet d’importer tous les modules métier (`backend.components.metiers.administration_publique`, etc.) sans erreur.
- Cette commande est compatible Linux/Bash (par défaut dans ce projet).
- Pour les tests JavaScript, utilisez :

```bash
npm test --prefix backend/components/metiers/administration_publique
```

**Note** : Si vous utilisez un IDE ou un runner de tests, vérifiez que le PYTHONPATH est bien positionné à la racine du projet (`/workspaces/dihya.io`).

---

## Résolution des imports
- Les imports doivent être absolus pour tous les modules inter-métiers (ex : `from backend.components.metiers.administration_publique...`).
- Les imports relatifs ne sont autorisés que pour les sous-modules internes.
- Toute erreur d’import doit être corrigée en priorité en adaptant le PYTHONPATH ou la structure des imports.

---

## Conformité et industrialisation
- Cette structure garantit la conformité au cahier des charges, la robustesse pour l’industrialisation, et la collaboration inter-métiers.
- Toute modification de structure doit être documentée dans ce fichier.

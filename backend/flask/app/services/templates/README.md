# templates/services/ — Templates métiers dynamiques (Dihya Coding)

Ce dossier contient les templates Python dynamiques utilisés pour la génération automatique de projets selon le domaine métier (e-commerce, éducation, social, etc.).

## Objectif

- Offrir des squelettes de projet adaptés à chaque secteur d’activité.
- Permettre la personnalisation et l’extension sans modifier le cœur du backend.
- Garantir la sécurité, la modularité et la souveraineté logicielle.

## Bonnes pratiques

- Chaque template doit être documenté (fonction, structure, dépendances, domaine visé).
- Versionner chaque template pour assurer la traçabilité des évolutions.
- Valider la conformité métier, sécurité et accessibilité de chaque template.
- Prévoir une fonction `get_template()` par fichier, retournant la structure du template.
- Permettre l’ajout de nouveaux templates par simple ajout de fichier/module dans ce dossier.
- Ne jamais inclure de secrets, d’identifiants ou de données sensibles dans les templates.
- Prévoir des tests unitaires pour chaque template critique.

## Liste des templates fournis

- **ecommerce.py** : Template e-commerce (boutique, panier, paiement…)
- **education.py** : Template éducation (cours, élèves, enseignants…)
- **social.py** : Template réseau social (posts, messages, notifications…)

## Exemple d’utilisation

```python
from app.services.templates import get_template_for_domain

template = get_template_for_domain("ecommerce")
print(template)
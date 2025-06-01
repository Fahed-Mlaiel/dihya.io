# core

Documentation interne Dihya Coding.

## Objectif

Ce dossier centralise les helpers transversaux, classes de base, exceptions globales, constantes et outils communs à tout le backend Dihya Coding.  
Il vise à éviter la duplication de code, garantir la cohérence métier et faciliter la maintenance.

## Bonnes pratiques

- Toute classe ou fonction réutilisable doit être ici ou dans `utils/`.
- Documenter chaque helper, base class ou constante avec une docstring claire.
- Ne jamais inclure de logique métier spécifique à un module.
- Les exceptions personnalisées doivent hériter de `DihyaBaseException`.
- Ne jamais exposer d’informations sensibles dans les messages d’erreur.
- Centraliser les constantes globales (rôles, statuts, messages…) dans `constants.py`.
- Centraliser les fonctions de validation dans `validators.py`.

## Structure recommandée

```
core/
├── README.md
├── core.py           # Helpers et classes de base
├── exceptions.py     # Exceptions globales personnalisées
├── constants.py      # Constantes globales (rôles, statuts, messages…)
└── validators.py     # Fonctions de validation réutilisables
```

## Exemples d’utilisation

```python
from core.core import ServiceResponse, get_logger
from core.exceptions import ValidationError
from core.constants import ROLE_ADMIN, STATUS_READY
from core.validators import is_valid_email

logger = get_logger("dihya.core")
try:
    if not is_valid_email("test@dihya.coding"):
        raise ValidationError("Email invalide")
    # ... logique métier ...
except ValidationError as e:
    logger.error(str(e))
```

---

*Ce dossier fait partie de la documentation technique interne Dihya Coding.*
#audit/ — Audit log & traçabilité des actions sensibles (Dihya Coding)

Ce dossier centralise la gestion des logs d’audit pour toutes les actions sensibles ou critiques du backend Dihya Coding.

## Objectif

- Assurer la traçabilité, la conformité et la transparence des opérations (suppression, modification, accès admin, etc.).
- Permettre l’audit de sécurité, la détection d’incidents et la conformité RGPD/souveraineté.

## Bonnes pratiques

- Logger chaque action sensible avec horodatage, utilisateur, action, ressource, statut et détails.
- Ne jamais inclure de secrets ou de données confidentielles dans les logs.
- Restreindre l’accès aux logs d’audit aux administrateurs ou responsables conformité.
- Documenter le format des logs et les actions tracées.
- Prévoir un script d’analyse ou d’export des logs si besoin.

## Format recommandé

```
[timestamp ISO8601] | user | action | resource | status | détails optionnels
```

**Exemples :**
```
2025-05-15T12:34:56Z | alice | delete_project | project_id=42 | SUCCESS | Suppression validée par rôle admin
2025-05-15T12:35:10Z | bob | login | user_id=7 | FAIL | Mot de passe incorrect
```

## Sécurité

- Les logs d’audit doivent être stockés dans un dossier non public et protégés.
- Ne jamais exposer les logs d’audit en production sans contrôle d’accès strict.
- Prévoir une rotation et une purge régulière des logs d’audit.

## Exemple de module d’audit (à placer dans `audit/logger.py`)

```python
from datetime import datetime

AUDIT_LOG_FILE = "audit/audit.log"

def log_audit(user, action, resource, status, details=""):
    """
    Logge une action sensible dans le fichier d’audit.
    :param user: utilisateur concerné (str)
    :param action: action réalisée (str)
    :param resource: ressource cible (str)
    :param status: résultat (SUCCESS/FAIL)
    :param details: informations complémentaires (str)
    """
    entry = f"{datetime.utcnow().isoformat()}Z | {user} | {action} | {resource} | {status} | {details}"
    with open(AUDIT_LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry + "\n")
```

## Script d’analyse (optionnel)

Pour faciliter l’audit, il est recommandé d’ajouter un script Python d’analyse ou d’export des logs (ex : `analyze_audit_log.py`).

---

**Équipe Dihya Coding**
# Tests automatisés des configurations backend (Dihya)

## Scripts fournis
- `validate_configs.py` : vérification syntaxe, cohérence, RGPD, sécurité, CI/CD

## Exécution

```bash
python3 validate_configs.py
```

## Ce qui est testé
- Syntaxe YAML, JSON, TOML (lint)
- Présence des champs critiques (app, security, rgpd, logging)
- RGPD : rétention, anonymisation, portabilité, suppression
- Sécurité : CORS, CSRF, allowed_hosts
- Arrêt immédiat en cas d’erreur

## RGPD & sécurité
- Pas de secrets dans les exemples
- Auditabilité et logs via CI/CD

# Tests automatisés des snippets backend (Dihya)

## Script fourni
- `test_snippets.sh` : exécution automatique de chaque snippet avancé (sécurité, monitoring, webhooks, validation, CI/CD)

## Exécution

```bash
bash test_snippets.sh
```

## Ce qui est testé
- Exécution de chaque snippet (sécurité, monitoring, webhooks, validation, CI/CD)
- Logs, audit, RGPD, multilingue
- Arrêt immédiat en cas d’erreur

## RGPD & sécurité
- Pas de données personnelles persistées
- Auditabilité et logs via CI/CD

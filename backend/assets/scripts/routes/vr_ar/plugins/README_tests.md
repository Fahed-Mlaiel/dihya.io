# Tests automatisés des plugins dynamiques vr_ar (Dihya)

## Script fourni
- `test_plugins.sh` : exécution automatique de chaque plugin, vérification hooks, RGPD, audit, i18n, accessibilité

## Exécution

```bash
bash test_plugins.sh
```

## Ce qui est testé
- Exécution de chaque plugin (audit, RGPD, i18n, accessibilité)
- Hooks dynamiques, logs, anonymisation, traduction, accessibilité
- Arrêt immédiat en cas d’erreur

## RGPD & sécurité
- Pas de données personnelles persistées
- Auditabilité et logs via CI/CD

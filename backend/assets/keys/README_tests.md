# Tests automatisés des clés publiques backend (Dihya)

## Script fourni
- `test_keys.sh` : vérification format PEM, hash SHA256, CI/CD

## Exécution

```bash
bash test_keys.sh
```

## Ce qui est testé
- Format PEM (en-tête/footer)
- Hash SHA256 pour chaque clé (traçabilité, souveraineté)
- Arrêt immédiat en cas d’erreur

## Sécurité
- Jamais de clé privée dans ce dossier
- Auditabilité et logs via CI/CD

# Tests automatisés des métadonnées branding backend (Dihya)

## Scripts fournis
- `test_meta.sh` : vérification lint JSON, présence des champs critiques, multilingue, hash SHA256
- `test_meta.py` : équivalent Python, CI/CD, RGPD, souveraineté numérique

## Exécution

```bash
bash test_meta.sh
# ou
python3 test_meta.py
```

## Ce qui est testé
- Lint JSON (présence des champs critiques : name, description, tags, version, created, author)
- Description multilingue (fr, en obligatoires)
- Hash SHA256 pour chaque fichier (traçabilité, souveraineté)
- Arrêt immédiat en cas d’erreur

## RGPD & souveraineté
- Pas de données personnelles dans les métadonnées
- Auditabilité et logs via CI/CD

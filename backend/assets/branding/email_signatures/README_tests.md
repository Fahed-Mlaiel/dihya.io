# Tests automatisés des signatures email backend (Dihya)

## Scripts fournis
- `test_signatures.sh` : vérification accessibilité HTML, présence ARIA, métadonnées, hash SHA256
- `test_signatures.py` : équivalent Python, CI/CD, RGPD, souveraineté numérique

## Exécution

```bash
bash test_signatures.sh
# ou
python3 test_signatures.py
```

## Ce qui est testé
- Accessibilité HTML (attribut alt, aria-label)
- Présence et validité des métadonnées JSON multilingues
- Hash SHA256 pour chaque fichier (traçabilité, souveraineté)
- Arrêt immédiat en cas d’erreur

## RGPD & souveraineté
- Pas de données personnelles dans les signatures
- Auditabilité et logs via CI/CD

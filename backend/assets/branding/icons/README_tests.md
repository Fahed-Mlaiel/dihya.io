# Tests automatisés des icônes backend (Dihya)

## Scripts fournis
- `test_icons.sh` : vérification accessibilité SVG, présence ARIA, métadonnées, hash SHA256
- `test_icons.py` : équivalent Python, CI/CD, RGPD, souveraineté numérique

## Exécution

```bash
bash test_icons.sh
# ou
python3 test_icons.py
```

## Ce qui est testé
- Accessibilité SVG (balises <title>, <desc>, aria-labelledby, role="img")
- Présence et validité des métadonnées JSON multilingues
- Hash SHA256 pour chaque fichier (traçabilité, souveraineté)
- Arrêt immédiat en cas d’erreur

## RGPD & souveraineté
- Pas de données personnelles dans les icônes
- Auditabilité et logs via CI/CD

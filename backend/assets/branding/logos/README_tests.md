# Tests automatisés des logos backend (Dihya)

## Scripts fournis
- `test_logos.sh` : vérification accessibilité SVG, présence ARIA, métadonnées, hash SHA256
- `test_logos.py` : équivalent Python, CI/CD, RGPD, souveraineté numérique

## Exécution

```bash
bash test_logos.sh
# ou
python3 test_logos.py
```

## Ce qui est testé
- Accessibilité SVG (balises <title>, <desc>, aria-labelledby, role="img")
- Présence et validité des métadonnées JSON multilingues
- Hash SHA256 pour chaque fichier (traçabilité, souveraineté)
- Arrêt immédiat en cas d’erreur

## RGPD & souveraineté
- Pas de données personnelles dans les logos
- Auditabilité et logs via CI/CD

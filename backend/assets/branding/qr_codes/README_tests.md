# Tests automatisés des QR codes backend (Dihya)

## Scripts fournis
- `test_qr_codes.sh` : vérification accessibilité SVG, présence ARIA, métadonnées, hash SHA256
- `test_qr_codes.py` : équivalent Python, CI/CD, RGPD, souveraineté numérique

## Exécution

```bash
bash test_qr_codes.sh
# ou
python3 test_qr_codes.py
```

## Ce qui est testé
- Accessibilité SVG (balises <title>, <desc>, aria-labelledby, role="img")
- Présence et validité des métadonnées JSON multilingues
- Hash SHA256 pour chaque fichier (traçabilité, souveraineté)
- Arrêt immédiat en cas d’erreur

## RGPD & souveraineté
- Pas de données personnelles dans les QR codes
- Auditabilité et logs via CI/CD

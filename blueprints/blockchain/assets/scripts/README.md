# Scripts Lead Dev – Gestion des assets de sécurité blockchain

Ce dossier regroupe les scripts d’industrialisation pour l’optimisation, l’audit, la génération d’index et la validation CI/CD des assets de sécurité.

## Scripts inclus
- `optimize_and_audit.py` : optimisation, scan, audit, génération d’index
- `generate_alt_texts.py` : génération automatique de textes alternatifs multilingues
- `validate_assets.sh` : validation CI/CD (lint, nommage, licence, alt)

## Bonnes pratiques
- Exécuter ces scripts à chaque ajout/modification d’asset
- Intégrer `validate_assets.sh` dans le pipeline CI/CD
- Adapter/compléter selon les besoins métier et la stack

---

Pour toute évolution, suivre la checklist Lead Dev et valider en équipe.

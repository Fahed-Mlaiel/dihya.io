# Guide d’accessibilité et RGPD pour le module vr_ar

## Accessibilité
- Tous les endpoints sont documentés pour l’accessibilité (labels, descriptions, erreurs multilingues)
- Les assets (scènes, modèles 3D) sont fournis avec des métadonnées (langue, titre, description)
- Les retours d’API sont structurés pour les lecteurs d’écran
- Les tests incluent des scénarios d’accessibilité (API, assets)

## RGPD
- Export complet des données utilisateur (scènes, assets, logs d’audit)
- Suppression et anonymisation sur demande
- Consentement explicite pour la création de scène
- Journalisation des accès et modifications (audit)
- Documentation multilingue sur la gestion des données personnelles

## Bonnes pratiques
- Utiliser les scripts d’export/import RGPD fournis
- Vérifier la conformité des fixtures et assets
- Consulter la documentation multilingue pour les obligations légales

Voir les fichiers audit.py, scripts/rgpd_export.sh, fixtures.json, et README_multilingue.md pour plus de détails.

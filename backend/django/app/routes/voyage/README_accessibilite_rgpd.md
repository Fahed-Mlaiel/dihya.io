# Guide d’accessibilité et RGPD pour le module voyage

## Accessibilité
- Tous les endpoints sont documentés pour l’accessibilité (labels, descriptions, erreurs multilingues)
- Les assets (billets, itinéraires) sont fournis avec des métadonnées (langue, titre, description)
- Les retours d’API sont structurés pour les lecteurs d’écran
- Les tests incluent des scénarios d’accessibilité (API, assets)

## RGPD
- Export complet des données utilisateur (réservations, itinéraires, logs d’audit)
- Suppression et anonymisation sur demande
- Consentement explicite pour la réservation
- Journalisation des accès et modifications (audit)
- Documentation multilingue sur la gestion des données personnelles

## Bonnes pratiques
- Utiliser les scripts d’export/import RGPD fournis
- Vérifier la conformité des fixtures et assets
- Consulter la documentation multilingue pour les obligations légales

Voir les fichiers audit.py, scripts/rgpd_export.sh, fixtures.json, et README_multilingue.md pour plus de détails.

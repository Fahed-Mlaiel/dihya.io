# Scripts — Organisation des tests centralisés

Ce dossier regroupe tous les tests d’exemples (samples) pour les scripts d’automatisation, organisés par sous-dossier métier :

- `audit/` : scripts d’audit
- `backup/` : scripts de sauvegarde
- `compliance/` : scripts de conformité
- `restore/` : scripts de restauration
- `index.js` : point d’entrée centralisé ultra avancé pour tous les tests de scripts (import dynamique, exports clé en main, métadonnées, CI/CD ready)

Chaque sous-dossier contient les fichiers de tests correspondants, prêts à être exécutés ou intégrés dans les pipelines CI/CD.

## Logique avancée
- Tous les modules sont importés dynamiquement via `index.js`.
- Métadonnées métier, couverture, auteur, date de mise à jour incluses dans chaque module.
- Structure clé en main, extensible, conforme au cahier des charges Dihya.

---

*Ajoutez ici tout nouveau test script en respectant la structure et la logique métier. Dernière mise à jour : 2025-06-08.*

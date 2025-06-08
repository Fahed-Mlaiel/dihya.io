# Helpers — Organisation des tests centralisés

Ce dossier regroupe tous les tests d’exemples (samples) pour les helpers, organisés par sous-dossier métier :

- `logger/` : tests des helpers de journalisation (logger)
- `utils/` : tests des helpers utilitaires (utils)
- `index.js` : point d’entrée centralisé ultra avancé pour tous les tests helpers (import dynamique, exports clé en main, métadonnées, CI/CD ready)

Chaque sous-dossier contient les fichiers de tests correspondants, prêts à être exécutés ou intégrés dans les pipelines CI/CD.

## Logique avancée
- Tous les modules sont importés dynamiquement via `index.js`.
- Métadonnées métier, couverture, auteur, date de mise à jour incluses dans chaque module.
- Structure clé en main, extensible, conforme au cahier des charges Dihya.

---

*Ajoutez ici tout nouveau test helper en respectant la structure et la logique métier. Dernière mise à jour : 2025-06-08.*

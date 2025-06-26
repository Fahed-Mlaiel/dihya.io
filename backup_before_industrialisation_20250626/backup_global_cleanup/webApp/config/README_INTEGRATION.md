# Module Avancé

Ce module fait partie de la plateforme dihya.io et fournit des fonctionnalités prêtes pour la production.

## Fonctionnalités
- Service métier avancé
- Gestion des erreurs
- Extensible et maintenable

# Intégration de la configuration

Ce dossier centralise la configuration de l’application web dihya.io : endpoints API, variables d’environnement, et options de build.

## Structure
- `env.js` : variables d’environnement dynamiques
- `api.config.js` : endpoints et clés d’API
- `featureFlags.js` : activation/désactivation de modules

## Procédure d’intégration
1. Modifier les variables dans `env.js` selon l’environnement (dev, staging, prod).
2. Documenter chaque changement dans ce fichier.
3. Utiliser les helpers de validation pour garantir la cohérence des configs.

## Sécurité
- Ne jamais committer de secrets ou credentials dans ce dossier.
- Utiliser les variables d’environnement pour toute donnée sensible.

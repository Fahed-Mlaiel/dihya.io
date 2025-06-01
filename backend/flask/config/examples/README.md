# examples/ — Exemples de fichiers de configuration (Dihya Coding)

Ce dossier regroupe des exemples de fichiers de configuration pour le backend Flask Dihya Coding.

## Objectif

- Fournir des modèles de fichiers de configuration pour faciliter l’installation, le déploiement et la maintenance du projet.
- Documenter les paramètres essentiels, leur usage, les valeurs recommandées et les bonnes pratiques de sécurité.
- Aider les nouveaux contributeurs et les équipes DevOps à configurer rapidement un environnement conforme.

## Bonnes pratiques

- Ne jamais inclure de secrets ou de données sensibles réelles dans les exemples.
- Documenter chaque paramètre (usage, valeurs possibles, sécurité).
- Proposer des valeurs par défaut sûres et adaptées à un environnement de développement.
- Prévoir des exemples pour chaque environnement clé (développement, test, production).
- Mettre à jour les exemples à chaque évolution de la configuration applicative.

## Exemple de structure

- `.env.example` : variables d’environnement principales.
- `config.yaml.example` : configuration avancée au format YAML.
- `secrets_example.md` : documentation sur la gestion des secrets.

## Exemple d’utilisation

Copier le fichier d’exemple et l’adapter à votre environnement :

```bash
cp .env.example .env
cp config.yaml.example config.yaml
# Dihya Seed Scripts

## Description
Scripts avancés pour l’initialisation et le peuplement sécurisé de la base de données Dihya. Support multilingue, multitenant, audit, conformité RGPD.

## Fonctionnalités
- Génération de données de test multilingues
- Support IA pour génération réaliste (LLaMA, Mixtral, fallback open source)
- Sécurité (validation, audit, anonymisation)
- Gestion des rôles et permissions
- Extensible par plugins/metiers

## Usage
```bash
python3 seed_script.py --lang fr --tenant test
python3 seed_script.py --lang en --tenant prod
```

## Internationalisation
- Français, English, العربية, ⵜⴰⵎⴰⵣⵉⵖⵜ, Deutsch, 中文, 日本語, 한국어, Nederlands, עברית, فارسی, हिन्दी, Español

## Sécurité
- Validation stricte, auditabilité
- Logs exportables, anonymisation RGPD

## Extensibilité
- Ajout de templates métiers, plugins via API/CLI

## Contact
- [Dihya Project](https://github.com/dihya-coding)

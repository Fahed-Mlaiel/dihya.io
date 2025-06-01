# Dihya Backup Scripts

## Description
Scripts avancés de sauvegarde et restauration pour la plateforme Dihya. Sécurité maximale, multilingue, auditabilité, conformité RGPD.

## Fonctionnalités
- Sauvegarde chiffrée (AES-256, rotation clés)
- Restauration sécurisée, logs d’accès
- Support multitenant, rôles (admin, user, invité)
- Export/import multi-format (enc, zip, tar.gz)
- Audit et traçabilité complète

## Usage
```bash
python3 backup_script.py --action backup --lang fr
python3 backup_script.py --action restore --lang en
```

## Internationalisation
- Français, English, العربية, ⵜⴰⵎⴰⵣⵉⵖⵜ, Deutsch, 中文, 日本語, 한국어, Nederlands, עברית, فارسی, हिन्दी, Español

## Sécurité
- Chiffrement bout-en-bout
- Validation des accès (JWT, RBAC)
- Logs d’audit exportables

## Extensibilité
- Plugins de sauvegarde/restauration via API/CLI

## Contact
- [Dihya Project](https://github.com/dihya-coding)

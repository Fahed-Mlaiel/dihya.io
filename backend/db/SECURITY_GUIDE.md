# Guide Sécurité – Dihya Backend DB

Ce guide détaille les bonnes pratiques de sécurité pour la base de données Dihya.

## Exigences
- Accès restreint (RBAC, MFA, logs)
- Chiffrement des données sensibles (password_hash, email)
- Conformité RGPD/NIS2 (anonymisation, suppression logique)
- Auditabilité (triggers, audit_logs)
- Sécurité réseau (firewall, accès IP, VPN)

## Procédures
- Toujours utiliser des comptes à privilèges minimaux
- Activer la journalisation des accès et modifications
- Tester la suppression logique et l’anonymisation
- Vérifier la conformité à chaque migration

## Références
- Voir `migrations/`, `database_schema.sql`, `tests/`
- [../specs/SECURITY_SPEC.md](../specs/SECURITY_SPEC.md)

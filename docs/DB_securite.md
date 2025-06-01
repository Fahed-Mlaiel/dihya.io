# Guide Sécurité Base de Données Dihya

## 1. Accès & Authentification
- Utilisez des comptes dédiés, MFA, ACL strictes
- Limitez les accès par IP, VPN obligatoire

## 2. Chiffrement
- Chiffrement au repos (AES-256)
- Chiffrement en transit (SSL/TLS)

## 3. Audit & RGPD
- Journalisation exhaustive (accès, modifications, exports)
- Anonymisation des exports et backups
- Droit à l’oubli et exportabilité

## 4. Monitoring
- Alertes sur accès suspects
- Rotation régulière des credentials

## 5. Exemples
- Utilisation de Vault pour la gestion des secrets
- Scripts d’audit automatisés

## 6. Ressources
- [DB_TROUBLESHOOTING.md](./DB_TROUBLESHOOTING.md)
- [DB_BACKUP_GUIDE.md](./DB_BACKUP_GUIDE.md)

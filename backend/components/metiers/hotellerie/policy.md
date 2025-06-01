# Hôtellerie – Politique de sécurité et conformité

- **RBAC** : Accès par rôle (admin, manager, client, invité)
- **JWT** : Authentification forte, expiration courte, rotation
- **CORS** : Origines restreintes, headers stricts
- **Validation** : Schémas stricts, anti-injection, anti-XSS
- **Audit** : Journalisation structurée, export RGPD, anonymisation
- **WAF** : Protection anti-DDOS, filtrage IP, détection d’anomalies
- **RGPD** : Consentement explicite, droit à l’oubli, portabilité
- **SEO** : Métadonnées, sitemap, robots.txt, logs structurés
- **i18n** : Détection automatique, fallback, accessibilité multilingue
- **Plugins** : Chargement dynamique, sandbox, auditabilité

## Exemples de règles
- Un invité ne peut pas créer/modifier/supprimer une réservation
- Un client peut gérer ses propres réservations
- Un manager peut gérer toutes les réservations
- Un admin peut tout gérer, exporter, auditer

---
© 2024 Dihya Coding. Open Source. RGPD-compliant.

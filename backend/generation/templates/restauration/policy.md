# Politique de gestion – Restauration

## Objectif
Garantir la sécurité, la conformité RGPD, l’équité, et la traçabilité dans la gestion de la restauration.

## Règles principales
- **Accès** :
  - Admin : tous droits
  - User : accès restreint à ses propres commandes
  - Invité : lecture anonymisée uniquement
- **Sécurité** :
  - Authentification JWT obligatoire
  - CORS strict, WAF, anti-DDOS
  - Audit logging activé
- **Confidentialité** :
  - Données sensibles chiffrées
  - Export/anonymisation sur demande
- **Multitenancy** :
  - Isolation stricte des tenants
- **RGPD** :
  - Consentement explicite, droit à l’oubli, portabilité
- **Auditabilité** :
  - Logs structurés, accès exportable

## Exemples de politiques
- Refus automatique d’accès hors rôle
- Notification en cas d’accès suspect
- Export CSV/JSON sécurisé

---
*Politique à adapter selon vos exigences métier et légales.*

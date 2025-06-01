# Politique de sécurité et conformité – Ressources Humaines (Dihya)

## Accès et rôles
- Accès restreint selon rôle (admin, user, invité)
- Authentification JWT obligatoire
- Multitenancy : chaque tenant a ses propres données et politiques

## Sécurité
- CORS strict, WAF, anti-DDOS, audit logging
- Validation stricte des entrées (type, format, longueur)
- Chiffrement des données sensibles (au repos et en transit)
- Anonymisation RGPD sur demande

## Conformité
- Export des données sur demande (format CSV/JSON)
- Journalisation des accès et modifications
- Suppression/anonymisation sur demande utilisateur

## Plugins
- Extension des politiques via plugins API/CLI

---

# Security & Compliance Policy – Human Resources (Dihya)

## Access & Roles
- Restricted access by role (admin, user, guest)
- Mandatory JWT authentication
- Multitenancy: each tenant has its own data and policies

## Security
- Strict CORS, WAF, anti-DDOS, audit logging
- Strict input validation (type, format, length)
- Encryption of sensitive data (at rest and in transit)
- GDPR anonymization on request

## Compliance
- Data export on request (CSV/JSON)
- Access and modification logging
- Deletion/anonymization on user request

## Plugins
- Policy extension via API/CLI plugins

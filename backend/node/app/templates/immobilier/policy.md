# Politique de sécurité – Immobilier (Dihya Coding)

## Accès & Rôles
- **Admin** : gestion complète, audit, export, plugins
- **Agent** : gestion des biens, offres, clients
- **Client** : consultation, soumission d’offres
- **Invité** : consultation limitée

## Sécurité
- CORS strict, JWT obligatoire, WAF, anti-DDOS
- Validation stricte des entrées (type, format, XSS, injection)
- Audit log (toutes actions sensibles)
- RGPD : anonymisation, export, consentement

## Multitenancy
- Isolation stricte des données par tenant

## Plugins
- Plugins validés, sandboxés, auditables

## IA
- Fallback open source (LLaMA, Mixtral, Mistral)

## Export
- Export CSV/JSON sécurisé, logs structurés

---

# Security Policy – Real Estate (EN)

*See French section above for full details.*

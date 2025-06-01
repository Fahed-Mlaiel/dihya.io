# Politique de gestion des previews (Dihya Coding)

## Sécurité
- CORS strict, JWT obligatoire, validation stricte des entrées
- Audit logging, WAF, anti-DDOS, sandboxing
- Chiffrement au repos et en transit

## RGPD & Confidentialité
- Anonymisation des données de preview
- Droit à l’oubli, export, logs d’accès

## Rôles & Multitenancy
- Admin : gestion complète
- User : génération/consultation
- Invité : consultation restreinte

## IA & Automatisation
- Génération automatique de previews (fallback LLaMA/Mixtral/Mistral)
- Détection de comportements suspects

## SEO & Accessibilité
- Génération automatique de logs structurés
- Accessibilité (WCAG, ARIA)

## Internationalisation
- Support fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es

## Plugins
- Extensible via API/CLI

---
Respect strict de la souveraineté numérique et des standards open source.

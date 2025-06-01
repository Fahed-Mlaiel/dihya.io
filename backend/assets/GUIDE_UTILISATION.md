# Dihya Backend Assets – Guide d’utilisation

Ce guide explique comment exploiter, enrichir et auditer les assets backend Dihya dans un contexte de production, CI/CD, multilingue, RGPD, plugins, auditabilité, accessibilité, souveraineté numérique.

## 1. Structure des assets
- Voir STRUCTURE.md pour la structure recommandée.
- Chaque sous-dossier (branding, templates, config, snippets, logs) a un README dédié.

## 2. Chargement et validation
- Utilisez `main.py` (Python) ou `index.js` (Node.js) pour charger, vérifier et auditer les assets.
- Les assets critiques sont validés par hash SHA-256, logs d’accès, audit RGPD.

## 3. Multilingue & accessibilité
- Tous les labels et templates sont multilingues (voir labels.multilingual.json).
- Les templates sont accessibles (WCAG 2.1, ARIA, tests fournis).

## 4. Plugins & extensibilité
- Les assets peuvent être enrichis par des plugins Python/Node.js (voir PLUGINS.md).
- Les hooks plugins permettent l’audit, l’anonymisation, l’enrichissement dynamique.

## 5. Audit, RGPD, souveraineté
- Voir AUDIT_RGPD.md et CI_CD_SOUVERAINETE.md pour les exigences de conformité.
- Les logs d’audit sont anonymisés, horodatés, versionnés.

## 6. Tests & CI/CD
- Les scripts de test valident l’intégrité, la conformité RGPD, la multilingue, l’accessibilité (voir TESTS.md).
- Les assets sont prêts pour l’intégration CI/CD, REST/GraphQL, multitenancy.

## 7. Exemples d’intégration
- Voir EXEMPLES_INTEGRATION.md pour des exemples Python, Node.js, REST/GraphQL, CI/CD.

## 8. Contribution
- Toute contribution doit respecter la sécurité, la RGPD, la souveraineté, la documentation intégrée.
- Documentez chaque ajout/modification d’asset dans les PR.

## 9. Support
- Pour toute question, voir README.md, assets.md, ou contactez l’équipe Dihya.

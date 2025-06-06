# Guide d’Accessibilité Construction

Ce guide détaille les bonnes pratiques d’accessibilité pour le métier Construction.

## Normes et standards
- Respect des WCAG 2.1 (AA minimum)
- Utilisation des rôles ARIA pour tous les composants interactifs
- Contrastes élevés, navigation clavier, focus visible
- Tests automatisés (axe, pa11y, Lighthouse)

## Checklist accessibilité
- Tous les formulaires sont accessibles au clavier
- Les couleurs sont testées pour le daltonisme
- Les images ont des textes alternatifs multilingues
- Les plugins métiers respectent l’accessibilité

## Outils recommandés
- axe-core, pa11y, Lighthouse, NVDA, VoiceOver

## Auditabilité
- Rapport d’audit accessibilité généré à chaque release (CI/CD)

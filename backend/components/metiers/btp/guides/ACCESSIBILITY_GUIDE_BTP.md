# Guide d’Accessibilité BTP

Ce guide détaille les bonnes pratiques d’accessibilité pour les applications BTP.

## Checklist accessibilité
- Respect des standards WCAG 2.2 AA/AAA
- Navigation clavier complète (tabindex, aria-label)
- Contrastes couleurs adaptés chantier (extérieur/intérieur)
- Plugins d’audit accessibilité automatisés (axe, pa11y, lighthouse)
- Tests utilisateurs (ouvriers, chefs de chantier, PMR)
- Export rapports accessibilité (JSON, HTML)
- Multilingue (fr, en, ar, de, etc.)
- RGPD : accessibilité des consentements

## Exemples de code
```html
<button aria-label="Créer un chantier">Créer</button>
```

## Plugins recommandés
- `accessibility-audit`
- `axe-core`
- `pa11y`

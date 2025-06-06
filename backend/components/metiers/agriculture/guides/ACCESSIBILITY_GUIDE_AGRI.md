# Guide d’Accessibilité Agriculture – Ultra avancé

Ce guide détaille toutes les exigences, bonnes pratiques, outils et tests d’accessibilité pour le module Agriculture (backend, API, plugins, templates, tests, CI/CD).

## Exigences
- Conformité RGAA/WCAG 2.2 AA/AAA
- API et templates compatibles ARIA, navigation clavier/voix
- Multilingue (fr, en, ar, tzm, de, zh, ja, ko, nl, he, fa, hi, es)
- Tests automatisés (axe, pa11y, Lighthouse, jest-axe)
- En-têtes HTTP : Content-Language, Content-Type, ARIA
- Accessibilité CLI et docs (Markdown, HTML, PDF)

## Tests
- `pytest tests/test_accessibility_e2e.py`
- ARIA, headers, multilingue, API/HTML

## Contribution
- Toute nouvelle route, template ou plugin doit être testé pour l’accessibilité.
- Voir ACCESSIBILITY_GUIDE.md pour la méthodologie Dihya.

---

*Guide exhaustif, multilingue, conforme RGPD, prêt à l’emploi.*

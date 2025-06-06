# GUIDE ACCESSIBILITÉ 3D – Dihya (FR)

Ce guide détaille toutes les bonnes pratiques, tests, outils et exigences d’accessibilité pour le module 3D (backend, API, plugins, templates, tests, CI/CD).

## Exigences
- Respect WCAG 2.2 AA/AAA
- API et templates compatibles ARIA, navigation clavier/voix
- Multilingue (fr, en, ar, tzm, de, zh, ja, ko, nl, he, fa, hi, es)
- Tests automatisés (axe, pa11y, Lighthouse)
- Headers HTTP : Content-Language, Content-Type, ARIA
- Accessibilité CLI et docs (Markdown, HTML, PDF)

## Tests
- `pytest tests/test_accessibility_e2e.py`
- Vérification ARIA, headers, multilingue, API/HTML

## Contribution
- Toute nouvelle route, template ou plugin doit être testé pour l’accessibilité.
- Voir ACCESSIBILITY_GUIDE.md global pour la méthodologie Dihya.

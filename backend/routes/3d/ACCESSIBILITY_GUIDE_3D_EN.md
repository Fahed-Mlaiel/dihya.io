# 3D ACCESSIBILITY GUIDE – Dihya (EN)

This guide details all best practices, tests, tools, and requirements for accessibility in the 3D module (backend, API, plugins, templates, tests, CI/CD).

## Requirements
- WCAG 2.2 AA/AAA compliance
- API and templates ARIA-compatible, keyboard/voice navigation
- Multilingual (fr, en, ar, tzm, de, zh, ja, ko, nl, he, fa, hi, es)
- Automated tests (axe, pa11y, Lighthouse)
- HTTP headers: Content-Language, Content-Type, ARIA
- CLI and docs accessibility (Markdown, HTML, PDF)

## Tests
- `pytest tests/test_accessibility_e2e.py`
- ARIA, headers, multilingual, API/HTML checks

## Contribution
- All new routes, templates, or plugins must be accessibility-tested.
- See global ACCESSIBILITY_GUIDE.md for Dihya methodology.

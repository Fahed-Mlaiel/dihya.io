# GUÍA DE ACCESIBILIDAD 3D – Dihya (ES)

Esta guía detalla todas las mejores prácticas, pruebas, herramientas y requisitos de accesibilidad para el módulo 3D (backend, API, plugins, plantillas, pruebas, CI/CD).

## Requisitos
- Cumplimiento WCAG 2.2 AA/AAA
- API y plantillas compatibles con ARIA, navegación por teclado/voz
- Multilingüe (fr, en, ar, tzm, de, zh, ja, ko, nl, he, fa, hi, es)
- Pruebas automatizadas (axe, pa11y, Lighthouse)
- Encabezados HTTP: Content-Language, Content-Type, ARIA
- Accesibilidad CLI y docs (Markdown, HTML, PDF)

## Pruebas
- `pytest tests/test_accessibility_e2e.py`
- Verificación ARIA, encabezados, multilingüe, API/HTML

## Contribución
- Toda nueva ruta, plantilla o plugin debe ser probado para accesibilidad.
- Ver ACCESSIBILITY_GUIDE.md global para la metodología Dihya.

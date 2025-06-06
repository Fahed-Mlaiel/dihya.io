# GUÍA RGPD 3D – Dihya (ES)

Esta guía detalla todos los requisitos, buenas prácticas, herramientas y pruebas RGPD para el módulo 3D (API, plugins, exportación, anonimización, logs, CI/CD).

## Requisitos
- Exportación/supresión RGPD, anonimización, logs exportables, auditabilidad
- Consentimiento del usuario, acceso exportable, supresión a petición
- Cumplimiento CI/CD, auditabilidad, monitorización

## Pruebas
- `pytest tests/test_rgpd.py`
- Exportación/anonimización/supresión, auditoría, logs RGPD

## Contribución
- Toda nueva ruta, plugin o plantilla debe ser conforme RGPD y probada.
- Ver LEGAL_COMPLIANCE_GUIDE.md global para la metodología Dihya.

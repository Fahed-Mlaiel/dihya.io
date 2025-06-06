# GUÍA DE SEGURIDAD 3D – Dihya (ES)

Esta guía detalla todos los requisitos, buenas prácticas, herramientas y pruebas de seguridad para el módulo 3D (API, plugins, RGPD, CI/CD).

## Requisitos
- CORS estricto, JWT obligatorio, WAF, anti-DDOS, validación estricta
- RBAC, logs estructurados, monitorización, auditabilidad
- Pruebas de intrusión automatizadas (XSS, inyección, fuerza bruta, anti-bot, CSRF)
- Exportación/supresión RGPD, anonimización, logs exportables

## Pruebas
- `pytest tests/test_security_e2e.py`
- Verificación fuerza bruta, XSS, inyección, anti-bot, CSRF

## Contribución
- Toda nueva ruta, plugin o plantilla debe ser probada para seguridad.
- Ver API_SECURITY_GUIDE.md global para la metodología Dihya.

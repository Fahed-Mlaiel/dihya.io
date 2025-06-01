# Guía de Onboarding para Dihya Coding (ES)

## Introducción
Dihya Coding es una plataforma open source para la gestión y desarrollo de proyectos de IA, VR, AR, web y móvil, con seguridad avanzada, internacionalización dinámica, extensibilidad y cumplimiento total de estándares globales (RGPD, auditoría, SEO, accesibilidad).

## Inicio rápido
1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/dihya-coding/dihya.git
   ```
2. **Configura el entorno:**
   - Asegúrate de tener Python 3.10+, Node.js 18+ y Docker.
   - Instala las dependencias:
     ```bash
     pip install -r requirements.txt
     npm install
     ```
3. **Ejecuta la aplicación:**
   ```bash
   make dev
   ```
4. **Inicia sesión:**
   - Usa la cuenta de invitado o regístrate desde la interfaz web.

## Seguridad y cumplimiento
- Todo el tráfico está cifrado (HTTPS).
- Autenticación JWT, CORS, WAF, anti-DDOS.
- Cumplimiento total RGPD, logs de auditoría, exportación de datos.

## Internacionalización
- Soporta: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.

## Contribución y soporte
- Consulta `CONTRIBUTING_ES.md`.
- Abre issues en [GitHub Issues](https://github.com/dihya-coding/dihya/issues).

## Ejemplo: Crear un nuevo proyecto IA
```bash
curl -X POST /api/projects -H 'Authorization: Bearer <token>' -d '{"type": "ia"}'
```

## Enlaces clave
- [Guía de seguridad](./securite_GUIDE_ES.md)
- [Roadmap](./ROADMAP_EN.md)
- [Documentación completa](./README_ES.md)

---
© 2025 Dihya Coding. Todos los derechos reservados.

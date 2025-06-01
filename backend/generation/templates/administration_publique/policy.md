# Administration Publique Policy

## Zugriffssteuerung (RBAC)
- Nur autorisierte Rollen (Admin, Sachbearbeiter, Auditor) dürfen sensible Verwaltungsdaten ändern.
- Alle API-Zugriffe werden mit JWT authentifiziert und geloggt.

## Datenschutz & GDPR
- Alle Verwaltungsdaten werden verschlüsselt gespeichert.
- Export/Import-Funktionen sind auditierbar und GDPR-konform.
- Opt-in/Opt-out für Tracking und Analytics.

## Sicherheit
- Input-Validierung, CORS, WAF, Anti-DDOS, Monitoring
- Regelmäßige Backups, Audit-Logs, Notfallwiederherstellung

## Barrierefreiheit
- Alle Verwaltungsfunktionen sind per Tastatur und Screenreader nutzbar (WCAG 2.2)

## Plugins & Erweiterbarkeit
- Externe Plugins müssen signiert und geprüft werden.
- Erweiterungen via /src/plugins möglich.

## CI/CD & Compliance
- Automatisierte Tests (Unit, Integration, Security, Accessibility)
- Policy-Checks im CI/CD

---
*English version below*

# Public Administration Policy

## Access Control (RBAC)
- Only authorized roles (Admin, Officer, Auditor) may modify sensitive data.
- All API access is JWT-authenticated and logged.

## Data Protection & GDPR
- All data is encrypted at rest.
- Export/import is auditable and GDPR-compliant.
- Opt-in/out for tracking/analytics.

## Security
- Input validation, CORS, WAF, anti-DDOS, monitoring
- Regular backups, audit logs, disaster recovery

## Accessibility
- All functions are keyboard/screenreader accessible (WCAG 2.2)

## Plugins & Extensibility
- External plugins must be signed and reviewed.
- Extensions via /src/plugins possible.

## CI/CD & Compliance
- Automated tests (unit, integration, security, accessibility)
- Policy checks in CI/CD

# E-Commerce – Sicherheits- und Compliance-Policy

- **RBAC**: Rollenbasiert (admin, shop-besitzer, kunde, gast)
- **JWT**: Starke Authentifizierung, kurze Gültigkeit, Rotation
- **CORS**: Strenge Ursprünge, restriktive Header
- **Validierung**: Strikte Schemata, Anti-Injection, Anti-XSS
- **Audit**: Strukturierte Logs, RGPD-Export, Anonymisierung
- **WAF**: Anti-DDOS, IP-Filter, Anomalie-Erkennung
- **RGPD**: Explizite Einwilligung, Recht auf Vergessen, Portabilität
- **SEO**: Metadaten, Sitemap, robots.txt, strukturierte Logs
- **i18n**: Automatische Erkennung, Fallback, barrierefrei
- **Plugins**: Dynamisches Laden, Sandbox, Auditierbarkeit

## Beispielregeln
- Gäste dürfen keine Bestellungen anlegen/ändern/löschen
- Kunden dürfen eigene Bestellungen verwalten
- Shop-Besitzer dürfen ihren Shop verwalten
- Admins dürfen alles verwalten, exportieren, auditieren

---
© 2024 Dihya Coding. Open Source. GDPR-konform.

# Dihya Coding – Handbuch (DE)

## Einführung
Dihya Coding ist eine Open-Source-Plattform für die Verwaltung und Entwicklung von KI-, VR-, AR-, Web- und Mobile-Projekten. Sie bietet höchste Sicherheit, dynamische Internationalisierung, Erweiterbarkeit, vollständige Auditierbarkeit und RGPD-Konformität.

## Schnellstart
1. **Repository klonen:**
   ```bash
   git clone https://github.com/dihya-coding/dihya.git
   ```
2. **Umgebung einrichten:**
   - Python 3.10+, Node.js 18+, Docker erforderlich.
   - Abhängigkeiten installieren:
     ```bash
     pip install -r requirements.txt
     npm install
     ```
3. **App starten:**
   ```bash
   make dev
   ```
4. **Anmelden:**
   - Gastkonto nutzen oder über das Web-UI registrieren.

## Sicherheit & Compliance
- HTTPS, JWT, CORS, WAF, Anti-DDOS
- RGPD-konform, Audit-Logs, Datenexport

## Internationalisierung
- Unterstützte Sprachen: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es

## Beitrag & Support
- Siehe `CONTRIBUTING_DE.md`.
- Issues auf [GitHub Issues](https://github.com/dihya-coding/dihya/issues) eröffnen.

## Beispiel: Neues KI-Projekt erstellen
```bash
curl -X POST /api/projects -H 'Authorization: Bearer <token>' -d '{"type": "ki"}'
```

## Wichtige Links
- [Sicherheitsleitfaden](./securite_GUIDE_DE.md)
- [Roadmap](./ROADMAP_DE.md)
- [Komplette Dokumentation](./README_DE.md)

---
© 2025 Dihya Coding. Alle Rechte vorbehalten.

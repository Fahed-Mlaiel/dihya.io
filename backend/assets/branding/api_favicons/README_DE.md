# Dihya Backend Assets – API Favicons (README DE)

Dieser Ordner enthält alle Backend-API-Favicons für Dihya Coding: SVG, PNG, mehrsprachig, barrierefrei, versioniert, auditierbar, DSGVO-konform, digital souverän, CI/CD-fähig, mit integrierter Dokumentation.

## Erweiterte Anforderungen
- **Barrierefreiheit**: Mehrsprachige Alt-Beschreibung (13 Sprachen), ARIA, AAA-Kontrast, automatisierte Tests
- **Mehrsprachigkeit**: Jedes Favicon hat Metadaten (alt, Beschreibung, Tags) in 13 Sprachen (siehe meta JSON)
- **Sicherheit**: Kein Frontend-Favicon, anonymisierte Zugriffsprotokolle, Auditierbarkeit
- **DSGVO**: Zugriffsprotokolle, Versionierung, integrierte Dokumentation
- **Souveränität**: Open Source, nachvollziehbar, auf souveräner Cloud gehostet
- **CI/CD**: Automatisierte Tests (SVG/PNG-Lint, Barrierefreiheit, SHA-256-Hash)
- **Auditierbarkeit**: Jedes kritische Favicon ist dokumentiert (Herkunft, Version, Hash, Nutzung, Compliance)
- **Modularität**: Erweiterbare Struktur (svg, png, meta)

## Empfohlene Struktur
api_favicons/
├── svg/                  # SVG-API-Favicons (mehrsprachig, barrierefrei, versioniert)
├── png/                  # PNG-API-Favicons (mehrsprachig, barrierefrei, versioniert)
├── meta/                 # Metadaten, Dokumentation, Historie, Audit
└── README_DE.md          # Diese Datei

## Beispiel-Metadaten
Siehe `meta_favicon-api.png.json` und `meta_favicon-api.json` für vollständige mehrsprachige Metadaten.

## Verwendung
- Automatische Integration in generierte Projekte (Web, Mobile, KI-Skripte)
- Barrierefreiheits-Audit über Plugin (`plugin_png_accessibility.py`)
- Automatisierter Test (`test_favicons_png.py`)
- Mehrsprachige Metadaten (`meta_favicon-api.png.json`)

## Sicherheit & DSGVO
- Anonymisierte, exportierbare, löschbare Zugriffsprotokolle (Recht auf Vergessenwerden)
- Strikte Zugriffsvalidierung (JWT, CORS, WAF, Anti-DDOS)
- Integrierte Dokumentation in jedem Asset und Plugin

## Tests
- Unittest: `test_favicons_png.py`
- Barrierefreiheits-Test: Plugin + CI
- DSGVO-Test: Anonymisierung, Export, Löschung

## Beitrag
- Fügen Sie Ihre Favicons in `svg/` oder `png/` mit mehrsprachigen Metadaten hinzu
- Dokumentieren Sie jede Ergänzung in `meta/`
- Überprüfen Sie die Konformität (Barrierefreiheit, DSGVO, Sicherheit, Audit)
- Führen Sie die Tests aus (`pytest`, `python3 test_favicons_png.py`)

© 2025 Dihya Coding – Open Source, AGPL, CC-BY-4.0

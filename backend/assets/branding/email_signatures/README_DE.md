# Dihya Backend Assets – E-Mail-Signaturen (README DE)

Dieser Ordner enthält alle Backend-E-Mail-Signaturen für Dihya Coding: HTML, TXT, mehrsprachig, barrierefrei, versioniert, auditierbar, DSGVO-konform, digital souverän, CI/CD-fähig, mit integrierter Dokumentation.

## Erweiterte Anforderungen
- **Barrierefreiheit**: Mehrsprachige Alt-Beschreibung, ARIA, AAA-Kontrast, automatisierte Tests
- **Mehrsprachigkeit**: Jede Signatur hat Metadaten (alt, Beschreibung, Tags) in 13 Sprachen (siehe meta JSON)
- **Sicherheit**: Anonymisierte Zugriffsprotokolle, Auditierbarkeit
- **DSGVO**: Zugriffsprotokolle, Versionierung, integrierte Dokumentation
- **Souveränität**: Open Source, nachvollziehbar, auf souveräner Cloud gehostet
- **CI/CD**: Automatisierte Tests (HTML/TXT-Lint, Barrierefreiheit, SHA-256-Hash)
- **Auditierbarkeit**: Jede kritische Signatur ist dokumentiert (Herkunft, Version, Hash, Nutzung, Compliance)
- **Modularität**: Erweiterbare Struktur (html, txt, meta)

## Empfohlene Struktur
email_signatures/
├── signature-backend-*.html / *.txt  # E-Mail-Signaturen (mehrsprachig, barrierefrei, versioniert)
├── meta_signature-backend-*.json    # Metadaten, Dokumentation, Historie, Audit
└── README_DE.md                     # Diese Datei

## Beispiel-Metadaten
Siehe `meta_signature-backend-*.json` für vollständige mehrsprachige Metadaten.

## Verwendung
- Automatische Integration in generierte E-Mails (Transaktionsmails)
- Barrierefreiheits-Audit über Plugin
- Automatisierter Test (`test_signatures_accessibility.py`)
- Mehrsprachige Metadaten (`meta_signature-backend-*.json`)

## Sicherheit & DSGVO
- Anonymisierte, exportierbare, löschbare Zugriffsprotokolle (Recht auf Vergessenwerden)
- Strikte Zugriffsvalidierung (JWT, CORS, WAF, Anti-DDOS)
- Integrierte Dokumentation in jedem Asset und Plugin

## Tests
- Unittest: `test_signatures_accessibility.py`
- Barrierefreiheits-Test: Plugin + CI
- DSGVO-Test: Anonymisierung, Export, Löschung

## Beitrag
- Fügen Sie Ihre Signaturen im passenden Format mit mehrsprachigen Metadaten hinzu
- Dokumentieren Sie jede Ergänzung in `meta_`
- Überprüfen Sie die Konformität (Barrierefreiheit, DSGVO, Sicherheit, Audit)
- Führen Sie die Tests aus (`pytest`, `python3 test_signatures_accessibility.py`)

© 2025 Dihya Coding – Open Source, AGPL, CC-BY-4.0

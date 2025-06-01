# Dihya Backend Assets – API Favicons (README EN)

This folder contains all backend API favicons for Dihya Coding: SVG, PNG, multilingual, accessible, versioned, auditable, GDPR-compliant, digitally sovereign, CI/CD-ready, with integrated documentation.

## Advanced Requirements
- **Accessibility**: Multilingual alt description (13 languages), ARIA, AAA contrast, automated tests
- **Multilingual**: Each favicon has metadata (alt, description, tags) in 13 languages (see meta JSON)
- **Security**: No frontend favicon, anonymized access logs, auditability
- **GDPR**: Access logs, versioning, integrated documentation
- **Sovereignty**: Open source, traceable, hosted on sovereign cloud
- **CI/CD**: Automated tests (SVG/PNG lint, accessibility, SHA-256 hash)
- **Auditability**: Each critical favicon is documented (origin, version, hash, usage, compliance)
- **Modularity**: Extensible structure (svg, png, meta)

## Recommended Structure
api_favicons/
├── svg/                  # SVG API favicons (multilingual, accessible, versioned)
├── png/                  # PNG API favicons (multilingual, accessible, versioned)
├── meta/                 # Metadata, documentation, history, audit
└── README.md             # This file

## Asset Metadata (example)
See `meta_favicon-api.png.json` and `meta_favicon-api.json` for full multilingual metadata.

## Usage
- Automatic integration in generated projects (web, mobile, AI scripts)
- Accessibility audit via plugin (`plugin_png_accessibility.py`)
- Automated test (`test_favicons_png.py`)
- Multilingual metadata (`meta_favicon-api.png.json`)

## Security & GDPR
- Anonymized, exportable, erasable access logs (right to be forgotten)
- Strict access validation (JWT, CORS, WAF, anti-DDOS)
- Integrated documentation in each asset and plugin

## Tests
- Unit test: `test_favicons_png.py`
- Accessibility test: plugin + CI
- GDPR test: anonymization, export, purge

## Contribution
- Add your favicons in `svg/` or `png/` with multilingual metadata
- Document each addition in `meta/`
- Check compliance (accessibility, GDPR, security, audit)
- Run tests (`pytest`, `python3 test_favicons_png.py`)

© 2025 Dihya Coding – Open Source, AGPL, CC-BY-4.0

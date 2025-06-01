# Validators-Modul – Dihya Coding

## DE
Dieses Modul bietet validierungsbezogene Hilfsfunktionen für alle Backend- und API-Komponenten. Es ist vollständig testbar, erweiterbar, konform (RGPD, SEO, i18n) und für Codespaces, Docker, K8s, CI optimiert.

**Features:**
- Feld-, Schema-, Rollen-, Policy-Validierung
- Multilingual: fr, en, ar, ber, de, zh, ja, ko, nl, he, fa, hi, es
- Erweiterbar durch Plugins und eigene Validatoren

**Nutzung:**
```python
from app.templates.validators import validate_schema
validate_schema({'email': 'test@example.com'}, {'email': 'email'})
```

**Compliance:**
- RGPD/DSGVO-konform, auditierbar, rollenbasiert, fallback AI

## EN
This module provides validation helpers for all backend/API components. Fully testable, extensible, compliant (GDPR, SEO, i18n), Codespaces/Docker/K8s/CI ready.

**Features:**
- Field, schema, role, policy validation
- Multilingual: fr, en, ar, ber, de, zh, ja, ko, nl, he, fa, hi, es
- Extensible via plugins and custom validators

**Usage:**
```python
from app.templates.validators import validate_schema
validate_schema({'email': 'test@example.com'}, {'email': 'email'})
```

**Compliance:**
- GDPR-compliant, auditable, role-based, fallback AI

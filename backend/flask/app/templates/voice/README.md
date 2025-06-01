# Voice-Modul – Dihya Coding

## DE
Dieses Modul bietet sichere, auditierbare Sprach-APIs (Text2Speech, Speech2Text, Voice-Bots) für alle Backend-Komponenten. Vollständig testbar, erweiterbar, konform (RGPD, SEO, i18n), Codespaces/Docker/K8s/CI ready.

**Features:**
- Text2Speech, Speech2Text, Voice-Bots, Multimandantenfähigkeit, Rollen, Audit, Logging
- Multilingual: fr, en, ar, ber, de, zh, ja, ko, nl, he, fa, hi, es
- Erweiterbar durch Plugins, fallback Open-Source-AI

**Nutzung:**
```python
from app.templates.voice import synthesize_speech
synthesize_speech('Hallo Welt', lang='de')
```

**Compliance:**
- RGPD/DSGVO-konform, auditierbar, rollenbasiert, fallback AI

## EN
This module provides secure, auditable voice APIs (Text2Speech, Speech2Text, voice bots) for all backend components. Fully testable, extensible, compliant (GDPR, SEO, i18n), Codespaces/Docker/K8s/CI ready.

**Features:**
- Text2Speech, Speech2Text, voice bots, multitenancy, roles, audit, logging
- Multilingual: fr, en, ar, ber, de, zh, ja, ko, nl, he, fa, hi, es
- Extensible via plugins, fallback open-source AI

**Usage:**
```python
from app.templates.voice import synthesize_speech
synthesize_speech('Hello world', lang='en')
```

**Compliance:**
- GDPR-compliant, auditable, role-based, fallback AI

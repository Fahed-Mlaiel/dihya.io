# Dihya Backend Assets – Exemples de Configurations

Exemple de configuration JSON (default.json) :
```json
{
  "app_name": "Dihya Backend",
  "version": "1.0.0",
  "log_level": "INFO",
  "audit": true,
  "languages": ["fr", "en", "de", "ar", "es", "it", "pt", "nl", "pl", "tr", "ru", "zh", "kab"],
  "plugins": ["audit", "rgpd", "accessibility"]
}
```

Exemple de configuration YAML (prod.yaml) :
```yaml
app_name: Dihya Backend
version: 1.0.0
env: production
log_level: WARNING
audit: true
languages:
  - fr
  - en
  - de
  - ar
  - es
  - it
  - pt
  - nl
  - pl
  - tr
  - ru
  - zh
  - kab
plugins:
  - audit
  - rgpd
  - accessibility
```

Exemple de configuration TOML (audit.toml) :
```toml
[app]
name = "Dihya Backend"
version = "1.0.0"

[audit]
enabled = true
log_level = "INFO"
```

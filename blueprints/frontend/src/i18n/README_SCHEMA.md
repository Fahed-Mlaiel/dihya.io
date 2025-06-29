# Schéma d’architecture i18n

```ascii
/i18n
  ├── i18n.js
  ├── autoTranslate.js
  ├── dialectSupport.js
  ├── localeUtils.js
  ├── index.js
  ├── BADGE_AUDIT.md
  ├── AUDIT_REPORT.json
  ├── CI_CD_GUIDE.md
  ├── locales/
  │     ├── fr.json, fr.js, en.json, en.js, ar.json, ar.js, ...
  │     ├── fr_BE.json, en_GB.json, pt_BR.json, ...
  │     └── auto/
  │           ├── auto_translate_template.json
  │           ├── detected_languages.json
  │           ├── fallbacks.json
  │           ├── audit_auto_locales.json
  │           ├── backup_*.json
  │           └── README.md
```

- Tous les scripts sont typés, documentés, testés.
- Les fichiers de langue sont dans `locales/` (un .json et un .js par langue/dialecte détecté).
- Les helpers (autoTranslate, dialectSupport, localeUtils) sont exportés via `index.js`.
- L’automatisation, l’audit et la CI/CD sont intégrés.

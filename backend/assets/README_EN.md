# Dihya Backend Assets – README (EN)

This folder contains all backend assets for the Dihya platform: scripts, configs, templates, test data, etc.

- Clear, versioned, secure structure
- Usage examples, conventions, import/export scripts
- Contribution, extension, customization

See [../README.md](../README.md)

---

## 📦 Role of the `backend/assets` folder

This folder centralizes all static resources, media, and files required for the backend operation of the Dihya Coding platform.

---

## 🧩 Typical content

- **Backend logos and branding** (for automatic doc generation, emails, etc.)
- **Static configuration files** (e.g.: secrets examples, default configs)
- **Static templates** (transactional emails, notifications, PDF reports)
- **Assets for code generation** (snippets, examples, backend blueprints)
- **Images or icons used by the backend** (e.g.: for report or export generation)
- **Log or audit exports** (timestamped, anonymized for GDPR compliance)

---

## 📁 Recommended structure
assets/ ├── branding/ # Backend logos, email signatures, API favicon ├── templates/ # Static templates (emails, reports, notifications) ├── config/ # Example config files ├── snippets/ # Backend code examples, blueprints, helpers ├── logs/ # Log/audit exports (GDPR, security) └── README.md # This file
---

## 🔒 Security & compliance

- **No personal data** should be stored here.
- **Logs and exports**: always anonymize and timestamp for GDPR compliance.
- **Restricted access**: only assets required by the backend should be present.
- **Auditability**: every asset addition/modification must be documented in PRs.

---

## ⚙️ Best practices

- **Clearly name** each file (e.g.: `template-reset-password.html`, `logo-backend.svg`).
- **Optimize** files for server use (size, format).
- **Version** critical assets for traceability.
- **Separate** frontend and backend assets to avoid confusion.

---

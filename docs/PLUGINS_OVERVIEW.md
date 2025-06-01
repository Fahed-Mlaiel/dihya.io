# Dihya Coding – Plugins Overview

## Introduction
The Dihya Coding platform features a robust, extensible plugin system. Plugins can be added, updated, or removed via API or CLI, enabling dynamic extension of backend, frontend, mobile, and AI functionalities without downtime.

## Key Features
- **API & CLI plugin management**
- **Hot-reload**: Plugins are loaded/unloaded at runtime
- **Security sandboxing**: Each plugin runs in an isolated context
- **Role-based access**: Plugins can define their own permissions
- **Internationalization**: Plugins support all platform languages
- **Auditability**: All plugin actions are logged (GDPR compliant)
- **Marketplace integration**: Discover and install plugins from a curated registry

## Plugin Types
- **Backend**: Add new API endpoints, business logic, AI integrations
- **Frontend**: UI components, dashboards, widgets
- **Mobile**: Native features, push notifications
- **AI**: Custom models, fallback logic, prompt templates

## Example: Adding a Plugin via API
```bash
curl -X POST /api/plugins \
  -H 'Authorization: Bearer <token>' \
  -F 'plugin=@my_plugin.zip'
```

## Security & Compliance
- Plugins are scanned for vulnerabilities before activation
- All actions are logged and auditable
- Plugins can be disabled or sandboxed at any time

## Documentation
- See [PLUGINS_README.md](./PLUGINS_README.md) for full developer and user documentation.

---
© 2025 Dihya Coding. All rights reserved.

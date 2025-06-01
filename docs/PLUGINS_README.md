# Dihya Coding – Plugins Developer & User Guide

## Introduction
This guide explains how to develop, install, manage, and secure plugins in the Dihya Coding platform. Plugins allow you to extend backend, frontend, mobile, and AI features dynamically, with full support for security, i18n, audit, and multitenancy.

## Plugin Structure
- `plugin.json`: Metadata (name, version, permissions, i18n)
- `main.py` or `main.js`: Entry point (Python or Node.js)
- `README.md`: Documentation (multilingual)
- `assets/`: Optional static files

## Development
1. **Scaffold a new plugin:**
   ```bash
   dihya plugins scaffold my_plugin
   ```
2. **Implement logic:**
   - Use provided API hooks (REST, GraphQL, events)
   - Add i18n support for all required languages
   - Define permissions in `plugin.json`
3. **Test locally:**
   ```bash
   make test-plugin PLUGIN=my_plugin
   ```
4. **Document:**
   - Provide usage, configuration, and security notes in all supported languages

## Installation
- **Via API:**
  ```bash
  curl -X POST /api/plugins -F 'plugin=@my_plugin.zip'
  ```
- **Via CLI:**
  ```bash
  dihya plugins install my_plugin.zip
  ```

## Security & Audit
- Plugins run in sandboxed environments
- All actions are logged (GDPR compliant)
- Plugins can be enabled/disabled per tenant or globally

## Example Plugin (Python)
```python
# main.py
def register(app):
    """Register plugin routes and hooks."""
    @app.route('/api/plugins/hello')
    def hello():
        return {"message": "Hello from plugin!"}
```

## Best Practices
- Always provide i18n for all user-facing strings
- Use type hints and docstrings
- Follow security guidelines (see `securite_GUIDE_EN.md`)

---
© 2025 Dihya Coding. All rights reserved.

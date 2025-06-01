# Dihya API Favicon – Export RGPD

Ce fichier permet l’export des métadonnées du favicon API backend Dihya, conforme RGPD, multilingue, accessibilité, audit, plugins, SEO.

- Format : JSON, CSV, YAML
- Export automatique via API ou CLI
- Exemple d’export :

```json
{
  "name": "Dihya API Favicon",
  "description": {"fr": "Favicon officiel de l’API backend Dihya..."},
  "version": "1.0.0",
  "created": "2025-05-22T00:00:00Z",
  ...
}
```

- Export CLI :
```bash
python meta_favicon_api.py --export json
```

- Export API :
```http
GET /api/meta/favicon?format=json
```

- RGPD : anonymisation, logs, audit, exportabilité, multilingue, accessibilité, plugins, SEO.

---

**Projet Dihya – Souveraineté numérique, sécurité, accessibilité, multilingue, auditabilité, production-ready.**

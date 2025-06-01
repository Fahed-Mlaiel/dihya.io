# Exemples d’appels GraphQL multilingues – Dihya Compliance

Ce document présente des exemples d’appels GraphQL pour l’API conformité/audit/plugins, en plusieurs langues (fr, en, ar).

## 🌍 Exemples d’appels GraphQL multilingues (toutes langues supportées)

### Français (fr)
```graphql
mutation ExportDonnees {
  exportData(input: {
    tenantId: "t1"
    userId: "u1"
    role: admin
    format: json
    lang: "fr"
  }) {
    status
    message
    exportUrl
    auditId
  }
}
```

### English (en)
```graphql
mutation ExportData {
  exportData(input: {
    tenantId: "t1"
    userId: "u1"
    role: admin
    format: json
    lang: "en"
  }) {
    status
    message
    exportUrl
    auditId
  }
}
```

### العربية (ar)
```graphql
mutation ExportData {
  exportData(input: {
    tenantId: "t1"
    userId: "u1"
    role: admin
    format: json
    lang: "ar"
  }) {
    status
    message
    exportUrl
    auditId
  }
}
```

### ⵜⴰ⎠ⵉⵖⵜ (amazigh/ber)
```graphql
mutation ExportData {
  exportData(input: {
    tenantId: "t1"
    userId: "u1"
    role: admin
    format: json
    lang: "ber"
  }) {
    status
    message
    exportUrl
    auditId
  }
}
```

### Deutsch (de)
```graphql
mutation ExportData {
  exportData(input: {
    tenantId: "t1"
    userId: "u1"
    role: admin
    format: json
    lang: "de"
  }) {
    status
    message
    exportUrl
    auditId
  }
}
```

### 中文 (zh)
```graphql
mutation ExportData {
  exportData(input: {
    tenantId: "t1"
    userId: "u1"
    role: admin
    format: json
    lang: "zh"
  }) {
    status
    message
    exportUrl
    auditId
  }
}
```

### 日本語 (ja)
```graphql
mutation ExportData {
  exportData(input: {
    tenantId: "t1"
    userId: "u1"
    role: admin
    format: json
    lang: "ja"
  }) {
    status
    message
    exportUrl
    auditId
  }
}
```

### 한국어 (ko)
```graphql
mutation ExportData {
  exportData(input: {
    tenantId: "t1"
    userId: "u1"
    role: admin
    format: json
    lang: "ko"
  }) {
    status
    message
    exportUrl
    auditId
  }
}
```

### Nederlands (nl)
```graphql
mutation ExportData {
  exportData(input: {
    tenantId: "t1"
    userId: "u1"
    role: admin
    format: json
    lang: "nl"
  }) {
    status
    message
    exportUrl
    auditId
  }
}
```

### עברית (he)
```graphql
mutation ExportData {
  exportData(input: {
    tenantId: "t1"
    userId: "u1"
    role: admin
    format: json
    lang: "he"
  }) {
    status
    message
    exportUrl
    auditId
  }
}
```

### فارسی (fa)
```graphql
mutation ExportData {
  exportData(input: {
    tenantId: "t1"
    userId: "u1"
    role: admin
    format: json
    lang: "fa"
  }) {
    status
    message
    exportUrl
    auditId
  }
}
```

### हिन्दी (hi)
```graphql
mutation ExportData {
  exportData(input: {
    tenantId: "t1"
    userId: "u1"
    role: admin
    format: json
    lang: "hi"
  }) {
    status
    message
    exportUrl
    auditId
  }
}
```

### Español (es)
```graphql
mutation ExportData {
  exportData(input: {
    tenantId: "t1"
    userId: "u1"
    role: admin
    format: json
    lang: "es"
  }) {
    status
    message
    exportUrl
    auditId
  }
}
```

## 🌍 Exemples d’appels GraphQL – Plugins (activation, multilingue)

### Activer un plugin (français)
```graphql
mutation ActivatePlugin {
  activatePlugin(input: {
    name: "audit-pro"
    lang: "fr"
  }) {
    status
    message
  }
}
```

### Activate a plugin (English)
```graphql
mutation ActivatePlugin {
  activatePlugin(input: {
    name: "audit-pro"
    lang: "en"
  }) {
    status
    message
  }
}
```

### تفعيل إضافة (arabe)
```graphql
mutation ActivatePlugin {
  activatePlugin(input: {
    name: "audit-pro"
    lang: "ar"
  }) {
    status
    message
  }
}
```

## 🌍 Exemples d’appels GraphQL – Cas d’erreur multilingues

### Export non autorisé (allemand)
```graphql
mutation ExportData {
  exportData(input: {
    tenantId: "t1"
    userId: "u1"
    role: guest
    format: json
    lang: "de"
  }) {
    status
    message
    exportUrl
    auditId
  }
}
```

### Export avec format invalide (japonais)
```graphql
mutation ExportData {
  exportData(input: {
    tenantId: "t1"
    userId: "u1"
    role: admin
    format: "pdf"
    lang: "ja"
  }) {
    status
    message
    exportUrl
    auditId
  }
}
```

## 🌍 Exemples d’appels GraphQL – Provenance (toutes langues supportées)

### Français (fr)
```graphql
mutation LogProvenance {
  logProvenance(input: {
    tenantId: "t1"
    userId: "u1"
    role: admin
    event: "export"
    details: {ip: "1.2.3.4"}
    lang: "fr"
  }) {
    status
    message
    auditId
  }
}
```

### English (en)
```graphql
mutation LogProvenance {
  logProvenance(input: {
    tenantId: "t1"
    userId: "u1"
    role: admin
    event: "export"
    details: {ip: "1.2.3.4"}
    lang: "en"
  }) {
    status
    message
    auditId
  }
}
```

### العربية (ar)
```graphql
mutation LogProvenance {
  logProvenance(input: {
    tenantId: "t1"
    userId: "u1"
    role: admin
    event: "export"
    details: {ip: "1.2.3.4"}
    lang: "ar"
  }) {
    status
    message
    auditId
  }
}
```

### ⵜⴰ⎠ⵉⵖⵜ (amazigh/ber)
```graphql
mutation LogProvenance {
  logProvenance(input: {
    tenantId: "t1"
    userId: "u1"
    role: admin
    event: "export"
    details: {ip: "1.2.3.4"}
    lang: "ber"
  }) {
    status
    message
    auditId
  }
}
```

### Deutsch (de)
```graphql
mutation LogProvenance {
  logProvenance(input: {
    tenantId: "t1"
    userId: "u1"
    role: admin
    event: "export"
    details: {ip: "1.2.3.4"}
    lang: "de"
  }) {
    status
    message
    auditId
  }
}
```

### 中文 (zh)
```graphql
mutation LogProvenance {
  logProvenance(input: {
    tenantId: "t1"
    userId: "u1"
    role: admin
    event: "export"
    details: {ip: "1.2.3.4"}
    lang: "zh"
  }) {
    status
    message
    auditId
  }
}
```

### 日本語 (ja)
```graphql
mutation LogProvenance {
  logProvenance(input: {
    tenantId: "t1"
    userId: "u1"
    role: admin
    event: "export"
    details: {ip: "1.2.3.4"}
    lang: "ja"
  }) {
    status
    message
    auditId
  }
}
```

### 한국어 (ko)
```graphql
mutation LogProvenance {
  logProvenance(input: {
    tenantId: "t1"
    userId: "u1"
    role: admin
    event: "export"
    details: {ip: "1.2.3.4"}
    lang: "ko"
  }) {
    status
    message
    auditId
  }
}
```

### Nederlands (nl)
```graphql
mutation LogProvenance {
  logProvenance(input: {
    tenantId: "t1"
    userId: "u1"
    role: admin
    event: "export"
    details: {ip: "1.2.3.4"}
    lang: "nl"
  }) {
    status
    message
    auditId
  }
}
```

### עברית (he)
```graphql
mutation LogProvenance {
  logProvenance(input: {
    tenantId: "t1"
    userId: "u1"
    role: admin
    event: "export"
    details: {ip: "1.2.3.4"}
    lang: "he"
  }) {
    status
    message
    auditId
  }
}
```

### فارسی (fa)
```graphql
mutation LogProvenance {
  logProvenance(input: {
    tenantId: "t1"
    userId: "u1"
    role: admin
    event: "export"
    details: {ip: "1.2.3.4"}
    lang: "fa"
  }) {
    status
    message
    auditId
  }
}
```

### हिन्दी (hi)
```graphql
mutation LogProvenance {
  logProvenance(input: {
    tenantId: "t1"
    userId: "u1"
    role: admin
    event: "export"
    details: {ip: "1.2.3.4"}
    lang: "hi"
  }) {
    status
    message
    auditId
  }
}
```

### Español (es)
```graphql
mutation LogProvenance {
  logProvenance(input: {
    tenantId: "t1"
    userId: "u1"
    role: admin
    event: "export"
    details: {ip: "1.2.3.4"}
    lang: "es"
  }) {
    status
    message
    auditId
  }
}
```

## 🌍 Exemples d’appels GraphQL – Audit (requêtes avancées)

### Requête d’audit par ID (français)
```graphql
query GetAudit {
  auditLog(auditId: "exp-123456") {
    auditId
    timestamp
    tenantId
    userId
    action
    status
    details
  }
}
```

### Requête d’audit filtrée (anglais)
```graphql
query AuditLogs {
  auditLogs(filter: {tenantId: "t1", action: "export"}) {
    auditId
    timestamp
    tenantId
    userId
    action
    status
    details
  }
}
```

## 🌍 Exemples d’appels GraphQL – Queries avancées multilingues

### Liste des exports (espagnol)
```graphql
query ListExports {
  exports(filter: {tenantId: "t1", format: "json", lang: "es"}) {
    exportId
    status
    message
    exportUrl
    auditId
  }
}
```

### Recherche de provenance (allemand)
```graphql
query ProvenanceSearch {
  provenanceLogs(filter: {tenantId: "t1", event: "export", lang: "de"}) {
    auditId
    timestamp
    tenantId
    userId
    event
    details
  }
}
```

### Statistiques d’audit (chinois)
```graphql
query AuditStats {
  auditStats(filter: {tenantId: "t1", lang: "zh"}) {
    totalExports
    totalProvenance
    lastExportDate
    lastProvenanceDate
  }
}
```

## Utilisation avec curl (GraphQL endpoint)

```bash
curl -X POST https://api.dihya.com/api/compliance/graphql/graphql \
  -H "Authorization: Bearer <JWT>" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "mutation ExportData { exportData(input: { tenantId: \"t1\", userId: \"u1\", role: admin, format: json, lang: \"fr\" }) { status message exportUrl auditId } }"
  }'
```

- Remplacez `lang` par la langue souhaitée (`fr`, `en`, `ar`, etc.) pour obtenir la réponse localisée.
- Les mutations et queries sont documentées dans [openapi_graphql_compliance.yaml](./openapi_graphql_compliance.yaml).

# Exemples d’appels GraphQL RGPD multilingues – Dihya Compliance

Ce document présente des exemples d’appels GraphQL RGPD (export, suppression, consentement, erreurs) pour toutes les langues supportées (fr, en, ar, ber, de, zh, ja, ko, nl, he, fa, hi, es).

## 🌍 Export RGPD (mutation)

### Français (fr)
```graphql
mutation ExportRGPD {
  exportRgpd(input: {
    userId: "u1"
    tenantId: "t1"
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
mutation ExportRGPD {
  exportRgpd(input: {
    userId: "u1"
    tenantId: "t1"
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
mutation ExportRGPD {
  exportRgpd(input: {
    userId: "u1"
    tenantId: "t1"
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

### ... (répéter pour ber, de, zh, ja, ko, nl, he, fa, hi, es)

## 🌍 Suppression RGPD (mutation)

### Français (fr)
```graphql
mutation DeleteRGPD {
  deleteRgpd(input: {
    userId: "u1"
    tenantId: "t1"
    role: admin
    lang: "fr"
  }) {
    status
    message
    auditId
  }
}
```

### ... (répéter pour toutes les langues)

## 🌍 Consentement RGPD (mutation)

### Français (fr)
```graphql
mutation ConsentRGPD {
  consentRgpd(input: {
    userId: "u1"
    tenantId: "t1"
    consent: true
    lang: "fr"
  }) {
    status
    message
    consent
    auditId
  }
}
```

### ... (répéter pour toutes les langues)

## 🌍 Exemples d’erreur et cas limites RGPD (GraphQL)

### Export non autorisé (rôle guest, allemand)
```graphql
mutation ExportRGPD {
  exportRgpd(input: {
    userId: "u1"
    tenantId: "t1"
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

### Suppression avec utilisateur inconnu (arabe)
```graphql
mutation DeleteRGPD {
  deleteRgpd(input: {
    userId: "unknown"
    tenantId: "t1"
    role: admin
    lang: "ar"
  }) {
    status
    message
    auditId
  }
}
```

### Consentement avec champ manquant (espagnol)
```graphql
mutation ConsentRGPD {
  consentRgpd(input: {
    userId: "u1"
    tenantId: "t1"
    lang: "es"
  }) {
    status
    message
    consent
    auditId
  }
}
```

### Export avec format invalide (japonais)
```graphql
mutation ExportRGPD {
  exportRgpd(input: {
    userId: "u1"
    tenantId: "t1"
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

- Les réponses d’erreur sont localisées et conformes RGPD, auditables, multilingues, plugins, sécurité maximale.

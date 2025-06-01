# Exemples d’appels API RGPD multilingues – Dihya Compliance

Ce document présente des exemples d’appels API RGPD (export, suppression, consentement) pour toutes les langues supportées (fr, en, ar, ber, de, zh, ja, ko, nl, he, fa, hi, es).

## 🌍 Export RGPD (POST /api/rgpd/export)

### Français (fr)
```bash
curl -X POST https://api.dihya.com/api/rgpd/export \
  -H "Authorization: Bearer <JWT>" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "u1",
    "tenant_id": "t1",
    "role": "admin",
    "format": "json",
    "lang": "fr"
  }'
```

### English (en)
```bash
curl -X POST https://api.dihya.com/api/rgpd/export \
  -H "Authorization: Bearer <JWT>" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "u1",
    "tenant_id": "t1",
    "role": "admin",
    "format": "json",
    "lang": "en"
  }'
```

### العربية (ar)
```bash
curl -X POST https://api.dihya.com/api/rgpd/export \
  -H "Authorization: Bearer <JWT>" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "u1",
    "tenant_id": "t1",
    "role": "admin",
    "format": "json",
    "lang": "ar"
  }'
```

### ... (répéter pour ber, de, zh, ja, ko, nl, he, fa, hi, es)

## 🌍 Suppression RGPD (POST /api/rgpd/delete)

### Français (fr)
```bash
curl -X POST https://api.dihya.com/api/rgpd/delete \
  -H "Authorization: Bearer <JWT>" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "u1",
    "tenant_id": "t1",
    "role": "admin",
    "lang": "fr"
  }'
```

### ... (répéter pour toutes les langues)

## 🌍 Consentement RGPD (POST /api/rgpd/consent)

### Français (fr)
```bash
curl -X POST https://api.dihya.com/api/rgpd/consent \
  -H "Authorization: Bearer <JWT>" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "u1",
    "tenant_id": "t1",
    "consent": true,
    "lang": "fr"
  }'
```

### ... (répéter pour toutes les langues)

## 🌍 Exemples d’erreur et cas limites RGPD (toutes langues)

### Export non autorisé (rôle guest, allemand)
```bash
curl -X POST https://api.dihya.com/api/rgpd/export \
  -H "Authorization: Bearer <JWT>" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "u1",
    "tenant_id": "t1",
    "role": "guest",
    "format": "json",
    "lang": "de"
  }'
```

### Suppression avec utilisateur inconnu (arabe)
```bash
curl -X POST https://api.dihya.com/api/rgpd/delete \
  -H "Authorization: Bearer <JWT>" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "unknown",
    "tenant_id": "t1",
    "role": "admin",
    "lang": "ar"
  }'
```

### Consentement avec champ manquant (espagnol)
```bash
curl -X POST https://api.dihya.com/api/rgpd/consent \
  -H "Authorization: Bearer <JWT>" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "u1",
    "tenant_id": "t1",
    "lang": "es"
  }'
```

### Export avec format invalide (japonais)
```bash
curl -X POST https://api.dihya.com/api/rgpd/export \
  -H "Authorization: Bearer <JWT>" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "u1",
    "tenant_id": "t1",
    "role": "admin",
    "format": "pdf",
    "lang": "ja"
  }'
```

- Remplacez `lang` par la langue souhaitée (`fr`, `en`, `ar`, `ber`, `de`, `zh`, `ja`, `ko`, `nl`, `he`, `fa`, `hi`, `es`) pour obtenir la réponse localisée.
- Les réponses sont localisées et conformes RGPD, auditables, plugins, multitenant, sécurité maximale.
- Les réponses d’erreur sont localisées et conformes RGPD, auditables, multilingues, plugins, sécurité maximale.

# Dihya Coding – Exemples d’Utilisation

Ce document présente des exemples complets pour exploiter toutes les fonctionnalités de la plateforme Dihya Coding : API, plugins, multitenancy, sécurité, internationalisation, génération de projets, etc.

## Sommaire
- Création d’un projet IA/VR/AR
- Appel API REST sécurisé (JWT, CORS)
- Utilisation GraphQL
- Ajout d’un plugin via API
- Internationalisation dynamique
- Export RGPD & audit
- Génération automatique de projet web/mobile/IA

---

### 1. Création d’un projet IA/VR/AR
```bash
curl -X POST https://api.dihya.dev/projects \
  -H 'Authorization: Bearer <JWT>' \
  -H 'Content-Type: application/json' \
  -d '{"name": "Projet IA Ultra", "type": "AI", "lang": "fr"}'
```

### 2. Appel API REST sécurisé
```bash
curl -X GET https://api.dihya.dev/projects/123 \
  -H 'Authorization: Bearer <JWT>' \
  -H 'Origin: https://frontend.dihya.dev'
```

### 3. Utilisation GraphQL
```graphql
query {
  project(id: "123") {
    name
    type
    owner {
      username
      role
    }
  }
}
```

### 4. Ajout d’un plugin via API
```bash
curl -X POST https://api.dihya.dev/plugins \
  -H 'Authorization: Bearer <JWT>' \
  -d '{"name": "plugin-llama-fallback", "source": "https://github.com/your-org/plugin-llama"}'
```

### 5. Internationalisation dynamique
```bash
curl -X PATCH https://api.dihya.dev/users/me \
  -H 'Authorization: Bearer <JWT>' \
  -d '{"lang": "ar"}'
```

### 6. Export RGPD & audit
```bash
curl -X GET https://api.dihya.dev/users/me/export \
  -H 'Authorization: Bearer <JWT>'
```

### 7. Génération automatique de projet
```bash
curl -X POST https://api.dihya.dev/generate \
  -H 'Authorization: Bearer <JWT>' \
  -d '{"type": "web", "template": "nextjs", "lang": "en"}'
```

---

Pour plus d’exemples : voir `docs/EXAMPLES_README.md` et les guides d’intégration.

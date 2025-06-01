# Exemples d’appels API/GraphQL du core Dihya (multilingue, plugins, audit)

## REST (Flask, Express)

### Génération automatique de projet

**FR**
```bash
curl -X POST http://localhost:8000/api/generate -H 'X-Dihya-Role: ai_user' -H 'X-Dihya-Lang: fr'
```
**EN**
```bash
curl -X POST http://localhost:8000/api/generate -H 'X-Dihya-Role: ai_user' -H 'X-Dihya-Lang: en'
```

### Authentification utilisateur
```bash
curl -X POST http://localhost:8000/api/auth/login
```

### Profil utilisateur (accès RBAC)
```bash
curl -X GET http://localhost:8000/api/user/profile -H 'X-Dihya-Role: user' -H 'X-Dihya-Lang: ar'
```

### Liste des plugins
```bash
curl -X GET http://localhost:8000/api/plugins -H 'X-Dihya-Role: user' -H 'X-Dihya-Lang: tzm'
```

### Liste des templates
```bash
curl -X GET http://localhost:8000/api/templates -H 'X-Dihya-Lang: fr'
```

## GraphQL

### Génération automatique de projet (GraphQL)
```bash
curl -X POST http://localhost:8000/graphql \
  -H 'Content-Type: application/json' \
  -d '{"query": "mutation { generateProject { status message } }"}'
```

### Exemple d’erreur RBAC (GraphQL)
```bash
curl -X POST http://localhost:8000/graphql \
  -H 'Content-Type: application/json' \
  -H 'X-Dihya-Role: guest' \
  -d '{"query": "mutation { generateProject { status message } }"}'
```

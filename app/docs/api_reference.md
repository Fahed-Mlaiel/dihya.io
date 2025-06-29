# Référence API

## Endpoints principaux

- `GET /api/v1/ressource` — Liste les ressources
- `POST /api/v1/ressource` — Crée une ressource
- `PUT /api/v1/ressource/:id` — Met à jour une ressource
- `DELETE /api/v1/ressource/:id` — Supprime une ressource

## Exemple d’appel

```bash
curl -X GET https://api.exemple.com/api/v1/ressource
```

## Schéma de réponse
```json
{
  "id": 1,
  "nom": "Exemple",
  "date": "2025-06-29"
}
```

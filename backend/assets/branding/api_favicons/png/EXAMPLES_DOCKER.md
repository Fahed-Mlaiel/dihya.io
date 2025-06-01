# Dihya API Favicons PNG – Exemples Docker

## Dockerfile pour serveur favicons Node.js
```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY . .
EXPOSE 4003
CMD ["node", "server.js"]
```

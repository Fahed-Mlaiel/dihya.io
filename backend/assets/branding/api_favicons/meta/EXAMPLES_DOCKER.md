# Dihya API Favicon – Exemples Docker

## Dockerfile pour serveur meta favicon Node.js
```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY . .
EXPOSE 4004
CMD ["node", "server.js"]
```

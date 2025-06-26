# Étape de build pour le backend
FROM node:16-alpine as backend-build
WORKDIR /app
COPY backend/package*.json ./
RUN npm ci --only=production
COPY backend/ ./
RUN npm run build

# Étape de build pour le frontend
FROM node:16-alpine as frontend-build
WORKDIR /app
COPY frontend/package*.json ./
RUN npm ci --only=production
COPY frontend/ ./
RUN npm run build

# Étape finale pour l'exécution
FROM node:16-alpine as runtime
WORKDIR /app

# Copie des artefacts de build du backend et du frontend
COPY --from=backend-build /app/build /app/backend
COPY --from=frontend-build /app/build /app/frontend

# Installation des dépendances de production pour le runtime
COPY --from=backend-build /app/node_modules /app/backend/node_modules

# Configuration des variables d'environnement
ENV NODE_ENV=production
ENV PORT=3000

# Exposition du port (peut varier selon la configuration)
EXPOSE 3000

# Commande pour démarrer l'application
CMD ["node", "backend/server.js"]

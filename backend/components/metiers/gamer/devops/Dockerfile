# Étape de build
FROM node:16-alpine as build-stage

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY gamer/package*.json ./

# Installer les dépendances
RUN npm install

# Copier les sources du projet
COPY gamer/ .

# Construire l'application
RUN npm run build

# Étape de production
FROM node:16-alpine as production-stage

# Définir le répertoire de travail
WORKDIR /app

# Copier les build artifacts de l'étape de build
COPY --from=build-stage /app/dist ./dist

# Copier les fichiers de dépendances (uniquement les dépendances de production)
COPY --from=build-stage /app/package*.json ./
RUN npm install --only=production

# Exposer le port sur lequel l'application va tourner
EXPOSE 3000

# Définir la commande pour démarrer l'application
CMD ["node", "dist/main.js"]

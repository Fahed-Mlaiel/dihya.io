# Définir l'image de base pour la construction
FROM node:16-alpine as build-stage

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de package et installer les dépendances
COPY agriculture/package*.json ./
RUN npm install

# Copier le reste du code source
COPY agriculture/ .

# Construire l'application pour la production
RUN npm run build

# Définir l'image de base pour l'exécution
FROM node:16-alpine as production-stage

# Définir le répertoire de travail
WORKDIR /app

# Copier les dépendances de production depuis l'étape de construction
COPY --from=build-stage /app/node_modules ./node_modules
COPY --from=build-stage /app/dist ./dist

# Exposer le port sur lequel le service va tourner
EXPOSE 3000

# Définir la commande pour exécuter l'application
CMD ["node", "dist/main.js"]

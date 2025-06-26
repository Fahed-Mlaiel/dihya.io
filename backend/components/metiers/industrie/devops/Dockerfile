# Étape de build
# Utilisation d'une image de base légère avec un environnement de build adéquat
FROM node:16-alpine as build-stage

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY industrie/package*.json ./

# Installer les dépendances
RUN npm install

# Copier les sources du projet
COPY industrie/ .

# Construire l'application
RUN npm run build

# Étape de production
# Utilisation d'une image de base légère pour l'exécution
FROM node:16-alpine as production-stage

# Définir le répertoire de travail
WORKDIR /app

# Copier les artefacts de build depuis l'étape de build
COPY --from=build-stage /app/dist ./dist

# Copier les dépendances nécessaires pour l'exécution
COPY --from=build-stage /app/node_modules ./node_modules

# Exposer le port sur lequel l'application va tourner
EXPOSE 3000

# Définir la commande pour démarrer l'application
CMD ["node", "dist/main.js"]

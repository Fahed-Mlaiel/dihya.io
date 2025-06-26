# Étape de build
# Utiliser une image de base officielle et légère, par exemple Node.js si "mode" est une application Node.js
FROM node:16-alpine AS build-stage

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY package*.json ./

# Installer les dépendances
RUN npm install

# Copier les sources de l'application
COPY . .

# Construire l'application pour la production
RUN npm run build

# Étape de production
# Utiliser une image de base légère pour l'exécution
FROM node:16-alpine AS production-stage

# Définir le répertoire de travail
WORKDIR /app

# Copier les artefacts de build depuis l'étape de build
COPY --from=build-stage /app/build ./build

# Copier les dépendances nécessaires pour l'exécution
COPY --from=build-stage /app/node_modules ./node_modules

# Exposer le port sur lequel l'application va tourner
EXPOSE 3000

# Définir la commande pour exécuter l'application
CMD ["node", "build/index.js"]

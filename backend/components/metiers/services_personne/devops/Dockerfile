# Étape de build
# Utilisation d'une image de base légère avec un SDK approprié pour la construction
FROM node:16-alpine as build-stage

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY services_personne/package*.json ./

# Installer les dépendances
RUN npm install

# Copier le reste des fichiers du projet
COPY services_personne/ .

# Construire l'application pour la production
RUN npm run build

# Étape de production
# Utilisation d'une image de base légère pour l'exécution
FROM node:16-alpine as production-stage

# Définir le répertoire de travail
WORKDIR /app

# Copier le build de l'étape précédente
COPY --from=build-stage /app/build ./build

# Copier les dépendances nécessaires pour l'exécution
COPY --from=build-stage /app/node_modules ./node_modules

# Exposer le port sur lequel l'application va tourner
EXPOSE 3000

# Définir la commande pour démarrer l'application
CMD ["node", "build/index.js"]

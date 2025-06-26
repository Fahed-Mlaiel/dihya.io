# Étape de build
# Utilisation d'une image de base légère avec un tag spécifique pour la prévisibilité
FROM node:16-alpine as build-stage

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de dépendances
COPY energie/package.json energie/yarn.lock ./

# Installer les dépendances en utilisant yarn
RUN yarn install --frozen-lockfile

# Copier les sources du projet
COPY energie/ .

# Construire l'application pour la production
RUN yarn build

# Étape de production
# Utilisation d'une image de base légère pour l'exécution
FROM node:16-alpine as production-stage

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les artefacts de build de l'étape précédente
COPY --from=build-stage /app/build ./build
COPY --from=build-stage /app/node_modules ./node_modules

# Exposer le port sur lequel l'application va s'exécuter
EXPOSE 3000

# Définir la commande pour démarrer l'application
CMD ["node", "build/index.js"]

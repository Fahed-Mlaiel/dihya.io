# Étape de build
# Utilisation d'une image de build avec tous les outils nécessaires
FROM node:16-alpine as builder

# Définir un répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY a_i/package.json a_i/yarn.lock ./

# Installer les dépendances
RUN yarn install --frozen-lockfile

# Copier le reste des fichiers du projet
COPY a_i/ .

# Construire l'application
RUN yarn build

# Étape de production
# Utilisation d'une image plus légère pour l'exécution
FROM node:16-alpine

# Définir un répertoire de travail
WORKDIR /app

# Copier les artefacts de build de l'étape précédente
COPY --from=builder /app/build ./build
COPY --from=builder /app/node_modules ./node_modules

# Définir la variable d'environnement pour le mode production
ENV NODE_ENV=production

# Exposer le port sur lequel l'application va tourner
EXPOSE 3000

# Commande pour démarrer l'application
CMD ["node", "build/index.js"]

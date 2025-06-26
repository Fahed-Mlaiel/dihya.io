# Étape de build
# Utilisation d'une image de base Node.js pour construire le code source
FROM node:16-alpine as builder

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de dépendances
COPY vr_ar/package.json vr_ar/yarn.lock ./

# Installer les dépendances
RUN yarn install --frozen-lockfile

# Copier le reste des fichiers du projet
COPY vr_ar/ .

# Construire l'application
RUN yarn build

# Étape de production
# Utilisation d'une image de base Node.js plus légère pour l'exécution
FROM node:16-alpine as production

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les dépendances de production depuis l'étape de build
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist

# Exposer le port sur lequel l'application s'exécute
EXPOSE 3000

# Définir la commande pour démarrer l'application
CMD ["node", "dist/main.js"]

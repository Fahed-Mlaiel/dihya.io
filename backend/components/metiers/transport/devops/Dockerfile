# Étape de build
FROM node:16-alpine as builder

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY transport/package.json transport/yarn.lock ./

# Installer les dépendances
RUN yarn install --frozen-lockfile

# Copier les sources du projet
COPY transport/ .

# Compiler le code si nécessaire (TypeScript, Babel, etc.)
# RUN yarn build

# Étape de production
FROM node:16-alpine as production

# Définir le répertoire de travail
WORKDIR /app

# Copier les dépendances de production depuis l'étape de build
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist

# Copier les autres fichiers nécessaires pour l'exécution
COPY transport/.env ./

# Exposer le port sur lequel l'application va tourner
EXPOSE 3000

# Définir la commande pour démarrer l'application
CMD ["node", "dist/index.js"]

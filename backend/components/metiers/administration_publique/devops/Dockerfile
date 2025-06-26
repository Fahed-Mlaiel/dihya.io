# Étape de build
# Utilisation d'une image de base Node.js légère
FROM node:16-alpine as builder

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de dépendances
COPY package*.json ./

# Installer les dépendances en mode production
RUN npm install --only=production

# Copier les sources de l'application
COPY . .

# Construire l'application si nécessaire (par exemple, TypeScript, Babel, etc.)
# RUN npm run build

# Étape de production
# Utilisation d'une nouvelle étape pour minimiser la taille de l'image finale
FROM node:16-alpine as production

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les dépendances installées depuis l'étape de build
COPY --from=builder /app/node_modules ./node_modules

# Copier les fichiers de build depuis l'étape de build
COPY --from=builder /app .

# Exposer le port sur lequel l'application va s'exécuter
EXPOSE 3000

# Définir la commande pour démarrer l'application
CMD ["node", "index.js"]

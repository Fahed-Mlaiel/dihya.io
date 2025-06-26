# Étape de build
# Utilisation d'une image de base Node.js officielle avec tag spécifique pour la prévisibilité
FROM node:16-alpine as builder

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Copie des fichiers de dépendances
COPY package*.json ./

# Installation des dépendances en mode production
RUN npm install --only=production

# Copie des sources de l'application
COPY . .

# Build de l'application si nécessaire (par exemple, TypeScript, Babel, etc.)
# RUN npm run build

# Étape de production
# Utilisation d'une image de base Node.js officielle avec tag spécifique pour la prévisibilité
FROM node:16-alpine as production

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Copie des dépendances et des builds depuis l'étape de build
COPY --from=builder /app .

# Exposition du port sur lequel l'application va tourner
EXPOSE 3000

# Définition de la commande pour démarrer l'application
CMD ["node", "server.js"]

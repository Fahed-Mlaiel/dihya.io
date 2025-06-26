# Étape de build pour les dépendances et la compilation des smart contracts
FROM node:16-alpine as builder

# Créer un répertoire de travail
WORKDIR /app

# Copier les fichiers de package.json et package-lock.json
COPY package*.json ./

# Installer les dépendances
RUN npm install --production

# Copier les sources du projet
COPY . .

# Compiler les smart contracts et autres éléments nécessaires
RUN npm run compile

# Étape de production pour exécuter l'application
FROM node:16-alpine as production

# Définir le répertoire de travail
WORKDIR /app

# Copier les dépendances de production depuis l'étape de build
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/build ./build
COPY --from=builder /app/package.json ./package.json

# Exposer le port sur lequel l'application va s'exécuter
EXPOSE 3000

# Définir la commande pour démarrer l'application
CMD ["npm", "start"]

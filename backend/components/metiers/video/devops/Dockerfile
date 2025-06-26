# Étape de build
# Utilisation d'une image de base Node.js légère
FROM node:16-alpine as builder

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY package*.json ./

# Installer les dépendances en mode production
RUN npm install --only=production

# Copier les sources du projet
COPY . .

# Construire l'application si nécessaire (étape à adapter selon le langage/framework)
RUN npm run build

# Étape finale
FROM node:16-alpine

# Définir le répertoire de travail
WORKDIR /app

# Copier les dépendances et les builds depuis l'étape de build
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist

# Copier les autres fichiers nécessaires pour l'exécution
COPY --from=builder /app/public ./public

# Exposer le port sur lequel le service "video" sera accessible
EXPOSE 3000

# Définir la commande pour démarrer l'application
CMD ["node", "dist/server.js"]

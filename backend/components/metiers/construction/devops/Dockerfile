# Étape de construction (build stage)
# Utilisation d'une image de base Node.js légère
FROM node:16-alpine AS builder

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY package*.json ./

# Installer les dépendances en mode production
RUN npm ci --only=production

# Copier les sources du projet
COPY . .

# Construire l'application si nécessaire (par exemple, TypeScript, Babel, etc.)
# RUN npm run build

# Étape de production (production stage)
# Utilisation d'une nouvelle étape pour minimiser la taille de l'image finale
FROM node:16-alpine AS production

# Définir le répertoire de travail
WORKDIR /app

# Copier les dépendances et les builds depuis l'étape de construction
COPY --from=builder /app .

# Exposer le port sur lequel l'application va s'exécuter
EXPOSE 3000

# Définir la commande pour exécuter l'application
CMD ["node", "server.js"]

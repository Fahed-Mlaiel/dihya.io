# Étape de build
# Utilisation d'une image de base Node.js légère
FROM node:16-alpine as builder

# Créer un répertoire pour l'application
WORKDIR /app

# Copier les fichiers de dépendances
COPY package*.json ./

# Installer les dépendances
RUN npm install --only=production

# Copier le reste du code source
COPY . .

# Compiler le code si nécessaire (par exemple, TypeScript, Babel, etc.)
# RUN npm run build

# Étape de production
FROM node:16-alpine as production

# Définir un utilisateur non privilégié
RUN adduser -D appuser
USER appuser

# Définir le répertoire de travail pour l'application
WORKDIR /app

# Copier les artefacts de build depuis l'étape de build
COPY --from=builder /app .

# Exposer le port sur lequel l'application va s'exécuter
EXPOSE 3000

# Commande pour exécuter l'application
CMD ["node", "index.js"]

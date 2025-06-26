# syntax=docker/dockerfile:1

# Étape de build
FROM node:16-alpine as build-stage

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY sante/package*.json ./

# Installer les dépendances
RUN npm install

# Copier les sources du projet
COPY sante/ .

# Construire l'application
RUN npm run build

# Étape de production
FROM nginx:1.21-alpine as production-stage

# Copier le build depuis l'étape de build
COPY --from=build-stage /app/build /usr/share/nginx/html

# Exposer le port (par défaut 80 pour nginx)
EXPOSE 80

# Commande pour démarrer nginx
CMD ["nginx", "-g", "daemon off;"]

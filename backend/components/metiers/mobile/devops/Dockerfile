# Étape de build
FROM node:16-alpine as builder

# Crée le répertoire de l'application
WORKDIR /app

# Installe les dépendances de l'application
# Utilise un fichier .dockerignore pour exclure les fichiers non nécessaires
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile

# Copie les fichiers de l'application
COPY . .

# Construit l'application pour la production
RUN yarn build

# Étape de production
FROM nginx:stable-alpine as production

# Copie les artefacts de build de l'étape précédente
COPY --from=builder /app/build /usr/share/nginx/html

# Copie la configuration Nginx personnalisée (si nécessaire)
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose le port (par défaut 80 pour Nginx)
EXPOSE 80

# Commande pour démarrer Nginx en foreground
CMD ["nginx", "-g", "daemon off;"]

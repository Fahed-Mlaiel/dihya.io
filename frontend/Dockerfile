# Dockerfile für das Frontend
FROM node:20-alpine
WORKDIR /app
COPY package.json ./
COPY package-lock.json ./
RUN npm install \
    && apk add --no-cache curl
COPY . .
RUN npm run build
CMD ["npm", "start"]

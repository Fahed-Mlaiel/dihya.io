# Ultra-advanced, secure, multilingual, extensible Node.js backend for Dihya
FROM node:20-alpine
LABEL maintainer="Dihya Team <opensource@dihya.org>"
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --omit=dev --no-audit --no-fund
COPY . .
EXPOSE 3001
HEALTHCHECK --interval=10s --timeout=5s --retries=5 CMD curl -f http://localhost:3001/health || exit 1
CMD ["node", "main.js"]


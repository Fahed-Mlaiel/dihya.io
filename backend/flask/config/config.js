/**
 * Dihya – Flask Backend Config (JS)
 * Multilingue, sécurisé, modulaire, souverain, documenté
 * Compatible Node.js/Flask (via node-flask interop)
 */

const dotenv = require('dotenv');
dotenv.config();

const config = {
  env: process.env.NODE_ENV || 'development',
  port: process.env.PORT || 5000,
  debug: process.env.DEBUG === 'true',
  secretKey: process.env.SECRET_KEY,
  allowedHosts: process.env.ALLOWED_HOSTS ? process.env.ALLOWED_HOSTS.split(',') : ['localhost'],
  cors: {
    origins: process.env.CORS_ORIGINS ? process.env.CORS_ORIGINS.split(',') : ['*'],
    credentials: true,
  },
  i18n: {
    default: 'fr',
    supported: ['fr', 'en', 'ar', 'tzr'],
  },
  logging: {
    level: process.env.LOG_LEVEL || 'info',
    file: process.env.LOG_FILE || './logs/app.log',
  },
  security: {
    csrf: true,
    xssProtection: true,
    contentSecurityPolicy: true,
  },
  tests: {
    enable: process.env.TESTS_ENABLE === 'true',
  },
};

module.exports = config;

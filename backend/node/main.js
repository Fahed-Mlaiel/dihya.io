// Ultra-advanced, secure, multilingual, extensible Node.js backend for Dihya
const express = require('express');
const helmet = require('helmet');
const cors = require('cors');
const morgan = require('morgan');
const rateLimit = require('express-rate-limit');
const i18next = require('i18next');
const i18nextMiddleware = require('i18next-http-middleware');
const Backend = require('i18next-fs-backend');
const dotenv = require('dotenv');
const fs = require('fs');
const path = require('path');

dotenv.config();

const app = express();

// Chargement des middlewares globaux avancés
const globalMiddlewares = require('./app/middlewares/global');
app.use(helmet());
app.use(cors(globalMiddlewares.corsOptions));
app.use(express.json());
app.use(morgan('combined'));
app.use(rateLimit({ windowMs: 15 * 60 * 1000, max: 200 }));

// i18n avancé (toutes langues du cahier des charges)
i18next
  .use(Backend)
  .use(i18nextMiddleware.LanguageDetector)
  .init({
    fallbackLng: 'en',
    preload: ['fr','en','ar','ber','de','zh','ja','ko','nl','he','fa','hi','es'],
    backend: { loadPath: path.join(__dirname, 'i18n/{{lng}}.json') },
    detection: { order: ['header', 'querystring', 'cookie'], caches: false },
  });
app.use(i18nextMiddleware.handle(i18next));

// Chargement dynamique de toutes les routes métiers
const routesPath = path.join(__dirname, 'app/routes');
fs.readdirSync(routesPath).forEach((dir) => {
  const routeFile = path.join(routesPath, dir, 'routes.js');
  if (fs.existsSync(routeFile)) {
    app.use(`/api/${dir}`, require(routeFile));
  }
});

// Health check
app.get('/health', (req, res) => res.status(200).json({ status: 'ok', uptime: process.uptime() }));
// Root
app.get('/', (req, res) => res.status(200).json({ message: req.t('welcome', { defaultValue: 'Welcome to Dihya Node Backend!' }) }));
// TODO: RGPD, plugins, audit, SEO, multitenancy, fallback IA, etc. pour répondre au cahier des charges

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
  console.log(`Dihya Node backend running on port ${PORT}`);
});

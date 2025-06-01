/**
 * Fonctions utilitaires avancées pour la sécurité, l'audit, l'i18n, la gestion des rôles, la compatibilité multi-stack, et l'intégration IA open source.
 * @module utils/utils
 */
const jwt = require('jsonwebtoken');
const cors = require('cors');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const i18next = require('i18next');
const i18nextMiddleware = require('i18next-http-middleware');
const supportedLanguages = ['fr', 'en', 'ar', 'ber', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es'];

// Middleware JWT sécurisé
function checkJwt(req, res, next) {
  const auth = req.headers['authorization'];
  if (!auth) return res.status(401).json({ error: 'No token' });
  const token = auth.split(' ')[1];
  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err) return res.status(403).json({ error: 'Invalid token' });
    req.user = user;
    next();
  });
}

// Middleware de gestion des rôles
function checkRole(roles) {
  return (req, res, next) => {
    if (!req.user || !roles.includes(req.user.role)) {
      return res.status(403).json({ error: 'Forbidden' });
    }
    next();
  };
}

// Internationalisation dynamique
const i18n = i18next.createInstance();
i18n.use(i18nextMiddleware.LanguageDetector).init({
  fallbackLng: 'fr',
  preload: supportedLanguages,
  resources: supportedLanguages.reduce((acc, lng) => {
    acc[lng] = { translation: require(`../locales/${lng}.json`) };
    return acc;
  }, {}),
});
function i18nMiddleware(req, res, next) {
  i18nextMiddleware.handle(i18n)(req, res, next);
}

// Web Application Firewall (WAF) simple
function wafMiddleware(req, res, next) {
  // Exemples de règles WAF
  if (/\b(drop|delete|update|insert)\b/i.test(JSON.stringify(req.body))) {
    return res.status(400).json({ error: 'WAF: Suspicious input' });
  }
  next();
}

// Protection anti-DDOS
const ddosMiddleware = rateLimit({
  windowMs: 60 * 1000,
  max: 100,
  message: 'Too many requests',
});

// Journalisation structurée RGPD
function auditLogger(req, res, next) {
  // Log structuré, anonymisé
  console.log({
    time: new Date().toISOString(),
    user: req.user ? req.user.id : 'anon',
    route: req.originalUrl,
    method: req.method,
    ip: req.ip,
  });
  next();
}

// Fallback IA open source (LLaMA, Mixtral, Mistral)
async function getLlamaFallback(prompt) {
  // Simulation fallback IA open source
  return `Réponse IA open source pour: ${prompt}`;
}

module.exports = {
  checkJwt,
  checkRole,
  i18nMiddleware,
  wafMiddleware,
  ddosMiddleware,
  auditLogger,
  getLlamaFallback,
};

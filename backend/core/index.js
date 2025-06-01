/**
 * Dihya – Backend Core Entrypoint (Node.js)
 * -----------------------------------------
 * Point d'entrée unique pour le cœur du backend Dihya (multi-stack, multilingue, souveraineté, sécurité).
 * - Fournit les services fondamentaux : configuration, logs, sécurité, i18n, gestion des rôles, utilitaires, middlewares
 * - Prêt pour intégration Node.js, CI/CD, Codespaces, cloud souverain
 * - Documentation multilingue, logs, conformité RGPD/NIS2, fallback open source
 *
 * 🇫🇷 Point d'entrée core backend Node.js (sécurité, logs, multilingue)
 * 🇬🇧 Node.js backend core entry point (secure, logs, multilingual)
 * 🇦🇪 نقطة دخول نواة الباكند (Node.js) مع الأمان والدعم متعدد اللغات
 * ⵣ Amuddu n core backend Node.js (amatu, logs, multilingual)
 */

const fs = require('fs');
const path = require('path');

// Gestion multilingue (i18n) ultra simple
const SUPPORTED_LANGS = ['fr', 'en', 'ar', 'tzm'];
function getLang(req) {
  return req.headers['x-dihya-lang'] && SUPPORTED_LANGS.includes(req.headers['x-dihya-lang'])
    ? req.headers['x-dihya-lang']
    : 'fr';
}

// Logger structuré (console, prêt pour extension ELK/SIEM)
function log(level, message, meta = {}) {
  const entry = {
    timestamp: new Date().toISOString(),
    level,
    message,
    ...meta
  };
  // En prod, remplacer par un logger structuré (Winston, Pino, etc.)
  console.log(JSON.stringify(entry));
}

// Middleware de gestion des rôles (RBAC)
const ROLES = ['admin', 'ai_user', 'auditor', 'user', 'guest'];
function rbac(requiredRole) {
  return (req, res, next) => {
    const userRole = req.headers['x-dihya-role'] || 'guest';
    if (!ROLES.includes(userRole) || ROLES.indexOf(userRole) < ROLES.indexOf(requiredRole)) {
      return res.status(403).json({
        error: {
          fr: "Accès refusé",
          en: "Access denied",
          ar: "وصول مرفوض",
          tzm: "Ulac tasireft"
        }[getLang(req)]
      });
    }
    next();
  };
}

// Middleware de sécurité HTTP (headers de base)
function securityHeaders(req, res, next) {
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.setHeader('X-Frame-Options', 'SAMEORIGIN');
  res.setHeader('X-XSS-Protection', '1; mode=block');
  res.setHeader('Referrer-Policy', 'strict-origin-when-cross-origin');
  res.setHeader('Permissions-Policy', 'geolocation=(), microphone=()');
  next();
}

// Utilitaire de chargement de configuration (JSON/YAML)
function loadConfig(configName) {
  const configPath = path.join(__dirname, 'configs', configName);
  if (!fs.existsSync(configPath)) throw new Error(`Config not found: ${configPath}`);
  const ext = path.extname(configPath).toLowerCase();
  const data = fs.readFileSync(configPath, 'utf-8');
  if (ext === '.json') return JSON.parse(data);
  if (ext === '.yaml' || ext === '.yml') {
    try {
      const yaml = require('js-yaml');
      return yaml.load(data);
    } catch (e) {
      throw new Error('js-yaml is required for YAML config parsing');
    }
  }
  throw new Error('Unsupported config file type');
}

module.exports = {
  getLang,
  log,
  rbac,
  ROLES,
  securityHeaders,
  loadConfig
};

/*
 * Utilisation dans une app Express :
 * const core = require('./backend/core');
 * app.use(core.securityHeaders);
 * app.use('/api/secure', core.rbac('admin'), secureRouter);
 * core.log('info', 'Démarrage du backend', { service: 'core' });
 *
 * Sécurité : logs, RBAC, headers, conformité RGPD/NIS2, fallback open source
 * Multilingue : prêt pour i18n (fr, en, ar, tzm)
 * Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution
 */

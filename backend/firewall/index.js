// Exemple de firewall/WAF Node.js ultra avancé pour Dihya
const express = require('express');
const rateLimit = require('express-rate-limit');
const helmet = require('helmet');
const cors = require('cors');
const jwt = require('jsonwebtoken');
const fs = require('fs');
const path = require('path');
const { createProxyMiddleware } = require('http-proxy-middleware');
const app = express();

app.use(helmet());
app.use(cors({ origin: ['https://dihya.app', 'http://localhost:3000'], credentials: true }));
app.use(express.json());

// Rate limiting/anti-DDOS
const limiter = rateLimit({ windowMs: 60 * 1000, max: 100 });
app.use(limiter);

// Audit/logs structurés
app.use((req, res, next) => {
  console.log(JSON.stringify({
    time: new Date().toISOString(),
    method: req.method,
    url: req.url,
    user: req.user ? req.user.id : null
  }));
  next();
});

// JWT auth middleware
app.use((req, res, next) => {
  const auth = req.headers['authorization'];
  if (auth && auth.startsWith('Bearer ')) {
    try {
      req.user = jwt.verify(auth.slice(7), process.env.JWT_SECRET || 'dev');
    } catch (e) {
      return res.status(401).json({ error: 'Invalid token' });
    }
  }
  next();
});

// Plugins sécurité dynamiques (exemple)
const plugins = {};
function registerPlugin(name, fn) { plugins[name] = fn; }
function getPlugin(name) { return plugins[name]; }
registerPlugin('audit', (req) => console.log('Audit plugin', req.url));

// RGPD export/anonymisation (exemple)
app.get('/export', (req, res) => {
  res.json({ logs: 'Exported logs (anonymized)' });
});

// Chargement dynamique des règles (modifiables à chaud)
function loadRule(file) {
  try {
    return JSON.parse(fs.readFileSync(path.join(__dirname, 'rules', file), 'utf-8'));
  } catch (e) {
    return null;
  }
}

// Middleware IP whitelist/blacklist
app.use((req, res, next) => {
  const whitelist = loadRule('ip_whitelist.json') || [];
  const blacklist = loadRule('ip_blacklist.json') || [];
  const ip = req.ip || req.connection.remoteAddress;
  if (blacklist.some(b => ip.startsWith(b))) return res.status(403).json({ error: 'IP bloquée' });
  if (whitelist.length && !whitelist.some(w => ip.startsWith(w))) return res.status(403).json({ error: 'IP non autorisée' });
  next();
});

// Middleware CORS dynamique
const corsRules = loadRule('cors_rules.json') || {};
app.use(cors({
  origin: corsRules.allowed_origins || ['https://dihya.app'],
  methods: corsRules.allowed_methods || ['GET', 'POST'],
  allowedHeaders: corsRules.allowed_headers || ['Authorization', 'Content-Type'],
  credentials: true
}));

// Middleware accès API par rôle
app.use((req, res, next) => {
  const apiAccess = loadRule('api_access.json') || {};
  const role = req.user && req.user.role ? req.user.role : 'guest';
  const allowed = apiAccess[role] || [];
  if (allowed.includes('*')) return next();
  if (allowed.some(route => req.url.startsWith(route))) return next();
  return res.status(403).json({ error: 'Accès API refusé pour ce rôle' });
});

// Reverse proxy interne : redirige vers l’API principale après filtrage
app.use('/api', createProxyMiddleware({
  target: process.env.DIHYA_API_URL || 'http://localhost:8000',
  changeOrigin: true,
  pathRewrite: { '^/api': '' },
  onProxyReq: (proxyReq, req) => {
    // Audit, logs, RGPD, etc. déjà appliqués par le firewall
  }
}));

app.listen(4000, () => console.log('Firewall/WAF Dihya running on 4000'));

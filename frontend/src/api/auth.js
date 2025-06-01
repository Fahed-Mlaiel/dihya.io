/**
 * @file auth.js
 * @description API centralisée pour l’authentification frontend Dihya Coding.
 * Sécurité avancée, conformité RGPD, auditabilité, extensibilité.
 * Toutes les requêtes sont validées, sécurisées, et loguées localement pour audit.
 * Ne jamais exposer de données sensibles sans consentement explicite.
 */

const API_BASE = '/api/auth';

/**
 * Inscription utilisateur.
 * @param {object} payload - { email, password, ... }
 * @returns {Promise<object>} Résultat de l’inscription
 */
export async function register(payload) {
  validateAuthPayload(payload);
  const res = await fetch(`${API_BASE}/register`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  const data = await res.json();
  logAuthEvent('register', payload.email);
  return data;
}

/**
 * Connexion utilisateur.
 * @param {object} payload - { email, password }
 * @returns {Promise<object>} Résultat de la connexion (token JWT, etc.)
 */
export async function login(payload) {
  validateAuthPayload(payload);
  const res = await fetch(`${API_BASE}/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  const data = await res.json();
  if (data.token) {
    localStorage.setItem('jwt_token', data.token);
  }
  logAuthEvent('login', payload.email);
  return data;
}

/**
 * Déconnexion utilisateur (suppression du token local).
 */
export function logout() {
  localStorage.removeItem('jwt_token');
  logAuthEvent('logout');
}

/**
 * Vérifie la validité du token JWT local.
 * @returns {boolean}
 */
export function isAuthenticated() {
  const token = localStorage.getItem('jwt_token');
  // Vérification simple, à renforcer côté backend
  return !!token;
}

/**
 * Valide le payload d’authentification.
 * @param {object} payload
 */
function validateAuthPayload(payload) {
  if (!payload || typeof payload !== 'object') throw new Error('Payload invalide');
  if (!payload.email || typeof payload.email !== 'string') throw new Error('Email requis');
  if (!payload.password || typeof payload.password !== 'string') throw new Error('Mot de passe requis');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} [email]
 */
function logAuthEvent(action, email) {
  try {
    const logs = JSON.parse(localStorage.getItem('auth_logs') || '[]');
    logs.push({
      action,
      email: email ? anonymizeEmail(email) : undefined,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('auth_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise un email pour les logs locaux.
 * @param {string} email
 * @returns {string}
 */
function anonymizeEmail(email) {
  if (!email) return '';
  const [user, domain] = email.split('@');
  return user[0] + '***@' + domain;
}

/**
 * Efface les logs d’authentification locaux (droit à l’oubli RGPD).
 */
export function clearLocalAuthLogs() {
  localStorage.removeItem('auth_logs');
}
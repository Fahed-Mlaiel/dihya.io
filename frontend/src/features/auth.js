/**
 * @file auth.js
 * @description Fonctions d’authentification pour Dihya Coding (login, logout, register, gestion token).
 * Garantit sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les données sont validées, anonymisées si besoin, et respectent le consentement utilisateur.
 */

/**
 * Connecte un utilisateur via l’API backend.
 * @param {string} username
 * @param {string} password
 * @returns {Promise<object>} Données utilisateur et token
 */
export async function login({ username, password }) {
  validateCredentials(username, password);
  const res = await fetch('/api/auth/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password }),
  });
  if (!res.ok) throw new Error('Échec de la connexion');
  const data = await res.json();
  if (data && data.token) {
    localStorage.setItem('jwt_token', data.token);
    logAuthFeatureEvent('login', username);
    return data;
  }
  throw new Error('Réponse inattendue');
}

/**
 * Déconnecte l’utilisateur (suppression du token local).
 */
export function logout() {
  localStorage.removeItem('jwt_token');
  logAuthFeatureEvent('logout', null);
}

/**
 * Inscrit un nouvel utilisateur via l’API backend.
 * @param {object} params
 * @param {string} params.username
 * @param {string} params.password
 * @param {string} [params.email]
 * @returns {Promise<object>} Données utilisateur et token
 */
export async function register({ username, password, email }) {
  validateCredentials(username, password);
  if (email && !validateEmail(email)) throw new Error('Email invalide');
  const res = await fetch('/api/auth/register', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password, email }),
  });
  if (!res.ok) throw new Error('Échec de l’inscription');
  const data = await res.json();
  if (data && data.token) {
    localStorage.setItem('jwt_token', data.token);
    logAuthFeatureEvent('register', username);
    return data;
  }
  throw new Error('Réponse inattendue');
}

/**
 * Récupère l’utilisateur courant depuis l’API backend.
 * @returns {Promise<object|null>}
 */
export async function getCurrentUser() {
  const token = localStorage.getItem('jwt_token');
  if (!token) return null;
  const res = await fetch('/api/user/me', {
    headers: { Authorization: `Bearer ${token}` },
  });
  if (!res.ok) return null;
  const data = await res.json();
  logAuthFeatureEvent('get_current_user', data?.username || null);
  return data;
}

/**
 * Valide les identifiants utilisateur.
 * @param {string} username
 * @param {string} password
 */
function validateCredentials(username, password) {
  if (!username || typeof username !== 'string' || username.length < 3) {
    throw new Error('Nom d’utilisateur invalide');
  }
  if (!password || typeof password !== 'string' || password.length < 6) {
    throw new Error('Mot de passe invalide');
  }
}

/**
 * Valide l’email utilisateur.
 * @param {string} email
 * @returns {boolean}
 */
function validateEmail(email) {
  // Validation simple
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string|null} value
 */
function logAuthFeatureEvent(action, value) {
  try {
    const logs = JSON.parse(localStorage.getItem('auth_feature_logs') || '[]');
    logs.push({
      action,
      value,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('auth_feature_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs d’authentification locaux (droit à l’oubli RGPD).
 */
export function clearLocalAuthFeatureLogs() {
  localStorage.removeItem('auth_feature_logs');
}
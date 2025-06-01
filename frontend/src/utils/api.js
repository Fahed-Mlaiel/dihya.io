/**
 * @file api.js
 * @description Utilitaire centralisé pour les appels API de Dihya Coding : gestion des requêtes HTTP, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

const API_BASE = process.env.API_BASE || 'http://localhost:3000/api';

/**
 * Effectue une requête GET sécurisée vers l’API.
 * @param {string} endpoint - Chemin relatif de l’API (ex: '/status')
 * @param {object} [options] - { headers, params, log }
 * @returns {Promise<object>} Réponse JSON ou erreur
 */
export async function apiGet(endpoint, options = {}) {
  if (!hasConsent()) return { success: false, error: 'Consentement requis' };
  try {
    const url = buildUrl(endpoint, options.params);
    const res = await fetch(url, {
      method: 'GET',
      headers: buildHeaders(options.headers)
    });
    const data = await res.json();
    if (options.log !== false) {
      logApiEvent('GET', endpoint, { status: res.status });
    }
    return { success: res.ok, data, status: res.status, error: res.ok ? null : data?.error || 'Erreur API' };
  } catch (err) {
    if (options.log !== false) {
      logApiEvent('GET_ERROR', endpoint, { error: err.message });
    }
    return { success: false, error: err.message };
  }
}

/**
 * Effectue une requête POST sécurisée vers l’API.
 * @param {string} endpoint - Chemin relatif de l’API (ex: '/auth/login')
 * @param {object} body - Corps de la requête
 * @param {object} [options] - { headers, log }
 * @returns {Promise<object>} Réponse JSON ou erreur
 */
export async function apiPost(endpoint, body, options = {}) {
  if (!hasConsent()) return { success: false, error: 'Consentement requis' };
  try {
    const url = buildUrl(endpoint);
    const res = await fetch(url, {
      method: 'POST',
      headers: buildHeaders(options.headers),
      body: JSON.stringify(body)
    });
    const data = await res.json();
    if (options.log !== false) {
      logApiEvent('POST', endpoint, { status: res.status });
    }
    return { success: res.ok, data, status: res.status, error: res.ok ? null : data?.error || 'Erreur API' };
  } catch (err) {
    if (options.log !== false) {
      logApiEvent('POST_ERROR', endpoint, { error: err.message });
    }
    return { success: false, error: err.message };
  }
}

/**
 * Construit une URL complète avec paramètres.
 * @param {string} endpoint
 * @param {object} [params]
 * @returns {string}
 */
function buildUrl(endpoint, params) {
  let url = API_BASE + (endpoint.startsWith('/') ? endpoint : '/' + endpoint);
  if (params && typeof params === 'object') {
    const query = Object.entries(params)
      .map(([k, v]) => encodeURIComponent(k) + '=' + encodeURIComponent(v))
      .join('&');
    if (query) url += '?' + query;
  }
  return url;
}

/**
 * Construit les headers pour la requête.
 * @param {object} [headers]
 * @returns {object}
 */
function buildHeaders(headers = {}) {
  const base = {
    'Content-Type': 'application/json'
  };
  // Ajoute le token d’auth si présent
  if (typeof window !== 'undefined' && window.localStorage) {
    const token = window.localStorage.getItem('auth_token');
    if (token) base['Authorization'] = `Bearer ${token}`;
  }
  return { ...base, ...headers };
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('api_utils_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} method
 * @param {string} endpoint
 * @param {object} data
 */
function logApiEvent(method, endpoint, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('api_utils_logs') || '[]');
    logs.push({
      method,
      endpoint: anonymizeEndpoint(endpoint),
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('api_utils_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise un endpoint pour les logs.
 * @param {string} endpoint
 * @returns {string}
 */
function anonymizeEndpoint(endpoint) {
  if (!endpoint) return '';
  return endpoint.replace(/\/[a-z0-9]{8,}/gi, '/***');
}

/**
 * Efface les logs API utils (droit à l’oubli RGPD).
 */
export function clearLocalApiUtilsLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('api_utils_logs');
  }
}

/* Documentation claire : chaque fonction est commentée pour auditabilité et conformité */
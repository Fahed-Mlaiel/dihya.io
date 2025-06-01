/**
 * @file generate.js
 * @description API centralisée pour la génération de projets côté frontend Dihya Coding.
 * Respecte la sécurité, la conformité RGPD, l’auditabilité et l’extensibilité.
 * Toutes les requêtes sont validées, sécurisées, et loguées localement pour audit.
 * Ne jamais exposer de données sensibles sans consentement explicite.
 */

const API_BASE = '/api/generate';

/**
 * Génère un projet à partir d’un cahier des charges (texte ou voix).
 * @param {object} payload - { description, type, options }
 * @returns {Promise<object>} Résultat de la génération (liens, code, logs…)
 */
export async function generateProject(payload) {
  validateGeneratePayload(payload);
  const token = localStorage.getItem('jwt_token');
  const res = await fetch(`${API_BASE}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`,
    },
    body: JSON.stringify(payload),
  });
  if (!res.ok) throw new Error('Erreur lors de la génération du projet');
  const data = await res.json();
  logGenerateEvent('generate', payload.type);
  return data;
}

/**
 * Liste les templates métiers disponibles (e-commerce, éducation, social, etc.).
 * @returns {Promise<Array>} Liste des templates
 */
export async function listTemplates() {
  const token = localStorage.getItem('jwt_token');
  const res = await fetch(`${API_BASE}/templates`, {
    headers: {
      'Authorization': `Bearer ${token}`,
    },
  });
  if (!res.ok) throw new Error('Erreur lors de la récupération des templates');
  return await res.json();
}

/**
 * Valide le payload de génération.
 * @param {object} payload
 */
function validateGeneratePayload(payload) {
  if (!payload || typeof payload !== 'object') throw new Error('Payload invalide');
  if (!payload.description || typeof payload.description !== 'string') throw new Error('Description requise');
  if (!payload.type || typeof payload.type !== 'string') throw new Error('Type de projet requis');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} type
 */
function logGenerateEvent(action, type) {
  try {
    const logs = JSON.parse(localStorage.getItem('generate_logs') || '[]');
    logs.push({
      action,
      type,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('generate_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de génération locaux (droit à l’oubli RGPD).
 */
export function clearLocalGenerateLogs() {
  localStorage.removeItem('generate_logs');
}
/**
 * @file preview.js
 * @description API centralisée pour la gestion des prévisualisations de projets sur Dihya Coding.
 * Respecte la sécurité, la conformité RGPD, l’auditabilité et l’extensibilité.
 * Toutes les requêtes sont validées, sécurisées, et loguées localement pour audit.
 * Ne jamais exposer de données sensibles sans consentement explicite.
 */

const API_BASE = '/api/preview';

/**
 * Récupère la prévisualisation d’un projet généré.
 * @param {string} projectId - Identifiant du projet à prévisualiser
 * @returns {Promise<object>} Données de prévisualisation (URL, status, logs…)
 */
export async function getPreview(projectId) {
  validateProjectId(projectId);
  const token = localStorage.getItem('jwt_token');
  const res = await fetch(`${API_BASE}?projectId=${encodeURIComponent(projectId)}`, {
    headers: {
      'Authorization': `Bearer ${token}`,
    },
  });
  if (!res.ok) throw new Error('Erreur lors de la récupération de la prévisualisation');
  const data = await res.json();
  logPreviewEvent('get_preview', projectId);
  return data;
}

/**
 * Liste les prévisualisations disponibles pour l’utilisateur.
 * @returns {Promise<Array>} Liste des prévisualisations
 */
export async function listPreviews() {
  const token = localStorage.getItem('jwt_token');
  const res = await fetch(`${API_BASE}/list`, {
    headers: {
      'Authorization': `Bearer ${token}`,
    },
  });
  if (!res.ok) throw new Error('Erreur lors de la récupération des prévisualisations');
  return await res.json();
}

/**
 * Supprime une prévisualisation (droit à l’oubli RGPD).
 * @param {string} previewId
 * @returns {Promise<object>} Résultat de la suppression
 */
export async function deletePreview(previewId) {
  validatePreviewId(previewId);
  const token = localStorage.getItem('jwt_token');
  const res = await fetch(`${API_BASE}/delete`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`,
    },
    body: JSON.stringify({ previewId }),
  });
  if (!res.ok) throw new Error('Erreur lors de la suppression de la prévisualisation');
  logPreviewEvent('delete', previewId);
  return await res.json();
}

/**
 * Valide l’identifiant de projet.
 * @param {string} projectId
 */
function validateProjectId(projectId) {
  if (!projectId || typeof projectId !== 'string') throw new Error('projectId invalide');
}

/**
 * Valide l’identifiant de prévisualisation.
 * @param {string} previewId
 */
function validatePreviewId(previewId) {
  if (!previewId || typeof previewId !== 'string') throw new Error('previewId invalide');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} id
 */
function logPreviewEvent(action, id) {
  try {
    const logs = JSON.parse(localStorage.getItem('preview_logs') || '[]');
    logs.push({
      action,
      id,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('preview_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de prévisualisation locaux (droit à l’oubli RGPD).
 */
export function clearLocalPreviewLogs() {
  localStorage.removeItem('preview_logs');
}
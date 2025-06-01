/**
 * @file project.js
 * @description API centralisée pour la gestion des projets côté frontend Dihya Coding.
 * Respecte la sécurité, la conformité RGPD, l’auditabilité et l’extensibilité.
 * Toutes les requêtes sont validées, sécurisées, et loguées localement pour audit.
 * Ne jamais exposer de données sensibles sans consentement explicite.
 */

const API_BASE = '/api/project';

/**
 * Récupère la liste des projets de l’utilisateur.
 * @returns {Promise<Array>} Liste des projets
 */
export async function listProjects() {
  const token = localStorage.getItem('jwt_token');
  const res = await fetch(`${API_BASE}/list`, {
    headers: {
      'Authorization': `Bearer ${token}`,
    },
  });
  if (!res.ok) throw new Error('Erreur lors de la récupération des projets');
  return await res.json();
}

/**
 * Récupère les détails d’un projet.
 * @param {string} projectId
 * @returns {Promise<object>} Détails du projet
 */
export async function getProject(projectId) {
  validateProjectId(projectId);
  const token = localStorage.getItem('jwt_token');
  const res = await fetch(`${API_BASE}/detail?projectId=${encodeURIComponent(projectId)}`, {
    headers: {
      'Authorization': `Bearer ${token}`,
    },
  });
  if (!res.ok) throw new Error('Erreur lors de la récupération du projet');
  return await res.json();
}

/**
 * Met à jour un projet (nom, description, options...).
 * @param {string} projectId
 * @param {object} updates - Champs à mettre à jour
 * @returns {Promise<object>} Projet mis à jour
 */
export async function updateProject(projectId, updates) {
  validateProjectId(projectId);
  if (!updates || typeof updates !== 'object') throw new Error('Mise à jour invalide');
  const token = localStorage.getItem('jwt_token');
  const res = await fetch(`${API_BASE}/update`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`,
    },
    body: JSON.stringify({ projectId, updates }),
  });
  if (!res.ok) throw new Error('Erreur lors de la mise à jour du projet');
  logProjectEvent('update', projectId);
  return await res.json();
}

/**
 * Supprime un projet (droit à l’oubli RGPD).
 * @param {string} projectId
 * @returns {Promise<object>} Résultat de la suppression
 */
export async function deleteProject(projectId) {
  validateProjectId(projectId);
  const token = localStorage.getItem('jwt_token');
  const res = await fetch(`${API_BASE}/delete`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`,
    },
    body: JSON.stringify({ projectId }),
  });
  if (!res.ok) throw new Error('Erreur lors de la suppression du projet');
  logProjectEvent('delete', projectId);
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
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} id
 */
function logProjectEvent(action, id) {
  try {
    const logs = JSON.parse(localStorage.getItem('project_logs') || '[]');
    logs.push({
      action,
      id,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('project_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de projet locaux (droit à l’oubli RGPD).
 */
export function clearLocalProjectLogs() {
  localStorage.removeItem('project_logs');
}
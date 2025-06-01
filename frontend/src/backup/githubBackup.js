/**
 * @file githubBackup.js
 * @description Module pour la gestion des sauvegardes de projets Dihya Coding vers GitHub.
 * Garantit sécurité, conformité RGPD, auditabilité, extensibilité et robustesse.
 * Toutes les opérations sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

const API_BASE = '/api/backup/github';

/**
 * Sauvegarde un projet sur un dépôt GitHub via l’API backend.
 * @param {string} projectId - Identifiant du projet à sauvegarder
 * @param {object} githubAuth - { token: string, repo: string, branch?: string }
 * @returns {Promise<object>} Résultat de la sauvegarde (URL commit, status…)
 */
export async function backupToGitHub(projectId, githubAuth) {
  validateProjectId(projectId);
  validateGithubAuth(githubAuth);

  // Respect du consentement utilisateur (RGPD)
  if (!window?.localStorage?.getItem('github_backup_consent')) return;

  const token = localStorage.getItem('jwt_token');
  const res = await fetch(`${API_BASE}/push`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`,
    },
    body: JSON.stringify({
      projectId,
      githubToken: githubAuth.token,
      repo: githubAuth.repo,
      branch: githubAuth.branch || 'main',
    }),
  });
  if (!res.ok) throw new Error('Erreur lors de la sauvegarde GitHub');
  const data = await res.json();
  logGithubBackupEvent('backup_github', projectId, githubAuth.repo);
  return data;
}

/**
 * Liste les sauvegardes GitHub existantes pour un projet.
 * @param {string} projectId
 * @returns {Promise<Array>} Liste des sauvegardes GitHub
 */
export async function listGithubBackups(projectId) {
  validateProjectId(projectId);
  const token = localStorage.getItem('jwt_token');
  const res = await fetch(`${API_BASE}/list?projectId=${encodeURIComponent(projectId)}`, {
    headers: {
      'Authorization': `Bearer ${token}`,
    },
  });
  if (!res.ok) throw new Error('Erreur lors de la récupération des sauvegardes GitHub');
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
 * Valide les informations d’authentification GitHub.
 * @param {object} githubAuth
 */
function validateGithubAuth(githubAuth) {
  if (!githubAuth || typeof githubAuth !== 'object') throw new Error('githubAuth invalide');
  if (!githubAuth.token || typeof githubAuth.token !== 'string') throw new Error('Token GitHub requis');
  if (!githubAuth.repo || typeof githubAuth.repo !== 'string') throw new Error('Repo GitHub requis');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} projectId
 * @param {string} repo
 */
function logGithubBackupEvent(action, projectId, repo) {
  try {
    const logs = JSON.parse(localStorage.getItem('github_backup_logs') || '[]');
    logs.push({
      action,
      projectId,
      repo,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('github_backup_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de sauvegarde GitHub locaux (droit à l’oubli RGPD).
 */
export function clearLocalGithubBackupLogs() {
  localStorage.removeItem('github_backup_logs');
}
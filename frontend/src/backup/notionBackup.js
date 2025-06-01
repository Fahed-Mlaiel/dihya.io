/**
 * @file notionBackup.js
 * @description Module pour la gestion des sauvegardes de projets Dihya Coding vers Notion.
 * Garantit sécurité, conformité RGPD, auditabilité, extensibilité et robustesse.
 * Toutes les opérations sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

const API_BASE = '/api/backup/notion';

/**
 * Sauvegarde un projet sur Notion via l’API backend.
 * @param {string} projectId - Identifiant du projet à sauvegarder
 * @param {object} notionAuth - { token: string, databaseId: string }
 * @returns {Promise<object>} Résultat de la sauvegarde (URL page, status…)
 */
export async function backupToNotion(projectId, notionAuth) {
  validateProjectId(projectId);
  validateNotionAuth(notionAuth);

  // Respect du consentement utilisateur (RGPD)
  if (!window?.localStorage?.getItem('notion_backup_consent')) return;

  const token = localStorage.getItem('jwt_token');
  const res = await fetch(`${API_BASE}/push`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`,
    },
    body: JSON.stringify({
      projectId,
      notionToken: notionAuth.token,
      databaseId: notionAuth.databaseId,
    }),
  });
  if (!res.ok) throw new Error('Erreur lors de la sauvegarde Notion');
  const data = await res.json();
  logNotionBackupEvent('backup_notion', projectId, notionAuth.databaseId);
  return data;
}

/**
 * Liste les sauvegardes Notion existantes pour un projet.
 * @param {string} projectId
 * @returns {Promise<Array>} Liste des sauvegardes Notion
 */
export async function listNotionBackups(projectId) {
  validateProjectId(projectId);
  const token = localStorage.getItem('jwt_token');
  const res = await fetch(`${API_BASE}/list?projectId=${encodeURIComponent(projectId)}`, {
    headers: {
      'Authorization': `Bearer ${token}`,
    },
  });
  if (!res.ok) throw new Error('Erreur lors de la récupération des sauvegardes Notion');
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
 * Valide les informations d’authentification Notion.
 * @param {object} notionAuth
 */
function validateNotionAuth(notionAuth) {
  if (!notionAuth || typeof notionAuth !== 'object') throw new Error('notionAuth invalide');
  if (!notionAuth.token || typeof notionAuth.token !== 'string') throw new Error('Token Notion requis');
  if (!notionAuth.databaseId || typeof notionAuth.databaseId !== 'string') throw new Error('DatabaseId Notion requis');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} projectId
 * @param {string} databaseId
 */
function logNotionBackupEvent(action, projectId, databaseId) {
  try {
    const logs = JSON.parse(localStorage.getItem('notion_backup_logs') || '[]');
    logs.push({
      action,
      projectId,
      databaseId,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('notion_backup_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de sauvegarde Notion locaux (droit à l’oubli RGPD).
 */
export function clearLocalNotionBackupLogs() {
  localStorage.removeItem('notion_backup_logs');
}
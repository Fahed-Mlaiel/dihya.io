/**
 * @file seo.js
 * @description API centralisée pour la gestion SEO côté frontend Dihya Coding.
 * Respecte la sécurité, la conformité RGPD, l’auditabilité et l’extensibilité.
 * Toutes les requêtes sont validées, sécurisées, et loguées localement pour audit.
 * Ne jamais exposer de données sensibles ou personnelles sans consentement explicite.
 */

const API_BASE = '/api/seo';

/**
 * Met à jour dynamiquement les balises meta SEO de la page.
 * @param {object} meta - { title, description, keywords, lang }
 */
export function updateMeta(meta) {
  validateMeta(meta);
  if (meta.title) document.title = meta.title;
  setOrUpdateMetaTag('description', meta.description);
  setOrUpdateMetaTag('keywords', meta.keywords);
  if (meta.lang) document.documentElement.lang = meta.lang;
  logSeoEvent('update_meta', meta.title || '');
}

/**
 * Récupère les recommandations SEO pour un projet donné.
 * @param {string} projectId
 * @returns {Promise<object>} Conseils SEO personnalisés
 */
export async function getSeoRecommendations(projectId) {
  validateProjectId(projectId);
  const token = localStorage.getItem('jwt_token');
  const res = await fetch(`${API_BASE}/recommendations?projectId=${encodeURIComponent(projectId)}`, {
    headers: {
      'Authorization': `Bearer ${token}`,
    },
  });
  if (!res.ok) throw new Error('Erreur lors de la récupération des recommandations SEO');
  logSeoEvent('get_recommendations', projectId);
  return await res.json();
}

/**
 * Valide la structure des meta données SEO.
 * @param {object} meta
 */
function validateMeta(meta) {
  if (!meta || typeof meta !== 'object') throw new Error('Meta invalide');
  if (meta.title && typeof meta.title !== 'string') throw new Error('Title invalide');
  if (meta.description && typeof meta.description !== 'string') throw new Error('Description invalide');
  if (meta.keywords && typeof meta.keywords !== 'string') throw new Error('Keywords invalide');
  if (meta.lang && typeof meta.lang !== 'string') throw new Error('Lang invalide');
}

/**
 * Ajoute ou met à jour une balise meta dans le head.
 * @param {string} name
 * @param {string} content
 */
function setOrUpdateMetaTag(name, content) {
  if (!content) return;
  let tag = document.querySelector(`meta[name="${name}"]`);
  if (!tag) {
    tag = document.createElement('meta');
    tag.setAttribute('name', name);
    document.head.appendChild(tag);
  }
  tag.setAttribute('content', content);
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
function logSeoEvent(action, id) {
  try {
    const logs = JSON.parse(localStorage.getItem('seo_logs') || '[]');
    logs.push({
      action,
      id,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('seo_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs SEO locaux (droit à l’oubli RGPD).
 */
export function clearLocalSeoLogs() {
  localStorage.removeItem('seo_logs');
}
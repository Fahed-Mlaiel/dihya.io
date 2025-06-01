/**
 * @file cmsPlugin.js
 * @description Plugin CMS pour Dihya Coding : gestion de contenu moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Plugin CMS Dihya Coding : expose les fonctions principales du CMS.
 */
const cmsPlugin = {
  name: 'cmsPlugin',
  version: '1.0.0',
  /**
   * Initialise le plugin CMS.
   * @param {object} [options] - { log: bool }
   * @returns {boolean} Succès de l’initialisation
   */
  init(options = {}) {
    if (!hasConsent()) return false;
    if (options.log !== false) {
      logCmsPluginEvent('init', { timestamp: new Date().toISOString() });
    }
    return true;
  },

  /**
   * Crée un contenu CMS.
   * @param {object} content - { title, body, author }
   * @param {object} [options] - { log: bool }
   * @returns {object} Résultat de la création
   */
  createContent(content, options = {}) {
    if (!hasConsent()) return { success: false, error: 'Consentement requis' };
    if (!validateContent(content)) {
      return { success: false, error: 'Contenu invalide' };
    }
    const stored = storeContent(anonymizeContent(content));
    if (options.log !== false) {
      logCmsPluginEvent('create', { title: anonymizeText(content.title), timestamp: new Date().toISOString() });
    }
    return { success: true, content: stored };
  },

  /**
   * Liste tous les contenus CMS.
   * @returns {Array<object>} Liste des contenus
   */
  listContents() {
    if (!hasConsent()) return [];
    try {
      const items = JSON.parse(window.localStorage.getItem('cms_contents') || '[]');
      return items;
    } catch {
      return [];
    }
  },

  /**
   * Supprime un contenu CMS par son identifiant.
   * @param {string} id
   * @param {object} [options] - { log: bool }
   * @returns {boolean} Succès de la suppression
   */
  deleteContent(id, options = {}) {
    if (!hasConsent()) return false;
    let items = [];
    try {
      items = JSON.parse(window.localStorage.getItem('cms_contents') || '[]');
      const idx = items.findIndex(item => item.id === id);
      if (idx === -1) return false;
      items.splice(idx, 1);
      window.localStorage.setItem('cms_contents', JSON.stringify(items));
      if (options.log !== false) {
        logCmsPluginEvent('delete', { id: anonymizeId(id), timestamp: new Date().toISOString() });
      }
      return true;
    } catch {
      return false;
    }
  }
};

/**
 * Stocke un contenu anonymisé dans le localStorage.
 * @param {object} content
 * @returns {object} Contenu stocké avec id
 */
function storeContent(content) {
  const items = JSON.parse(window.localStorage.getItem('cms_contents') || '[]');
  const id = generateId();
  const stored = { ...content, id, createdAt: new Date().toISOString() };
  items.push(stored);
  window.localStorage.setItem('cms_contents', JSON.stringify(items));
  return stored;
}

/**
 * Valide un contenu CMS.
 * @param {object} content
 * @returns {boolean}
 */
function validateContent(content) {
  return (
    content &&
    typeof content.title === 'string' &&
    content.title.length > 0 &&
    typeof content.body === 'string' &&
    content.body.length > 0
  );
}

/**
 * Génère un identifiant unique.
 * @returns {string}
 */
function generateId() {
  return Math.random().toString(36).slice(2, 10) + Date.now().toString(36).slice(-4);
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('cms_plugin_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logCmsPluginEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('cms_plugin_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('cms_plugin_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise un contenu pour le stockage/log.
 * @param {object} content
 * @returns {object}
 */
function anonymizeContent(content) {
  return {
    title: anonymizeText(content.title),
    body: '[texte anonymisé]',
    author: content.author ? anonymizeText(content.author) : undefined
  };
}

/**
 * Anonymise un texte pour les logs (ne conserve que la longueur).
 * @param {string} text
 * @returns {string}
 */
function anonymizeText(text) {
  if (!text) return '';
  return `[texte:${text.length} caractères]`;
}

/**
 * Anonymise un identifiant pour les logs.
 * @param {string} id
 * @returns {string}
 */
function anonymizeId(id) {
  if (!id) return '';
  return id.length > 8 ? id.slice(0, 2) + '***' + id.slice(-2) : '***';
}

/**
 * Efface les logs CMS plugin (droit à l’oubli RGPD).
 */
export function clearLocalCmsPluginLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('cms_plugin_logs');
  }
}

export default cmsPlugin;

/* Documentation claire : chaque fonction et composant est commenté pour auditabilité et conformité */
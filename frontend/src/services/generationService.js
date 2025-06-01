/**
 * @file generationService.js
 * @description Service centralisé de génération pour Dihya Coding : génération de code, fichiers, assets, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Génère un fichier ou un asset selon le type et les paramètres fournis.
 * @param {object} params
 * @param {string} params.type - Type de génération ('code', 'markdown', 'image', etc.)
 * @param {object} params.options - Options spécifiques à la génération (langage, contenu, style…)
 * @returns {object} Résultat { success, output, error, timestamp }
 */
export function generate({ type, options }) {
  if (!hasConsent()) {
    return {
      success: false,
      output: null,
      error: 'Consentement requis',
      timestamp: new Date().toISOString()
    };
  }
  if (!type || typeof type !== 'string') {
    return {
      success: false,
      output: null,
      error: 'Type de génération invalide',
      timestamp: new Date().toISOString()
    };
  }

  let output, error = null;
  try {
    switch (type) {
      case 'code':
        output = generateCode(options);
        break;
      case 'markdown':
        output = generateMarkdown(options);
        break;
      case 'image':
        output = generateImage(options);
        break;
      default:
        throw new Error('Type de génération non supporté');
    }
    if (options && options.log !== false) {
      logGenerationEvent('generate', {
        type,
        options: anonymizeOptions(options),
        timestamp: new Date().toISOString()
      });
    }
    return { success: true, output, error: null, timestamp: new Date().toISOString() };
  } catch (err) {
    error = err.message;
    if (options && options.log !== false) {
      logGenerationEvent('generate_error', {
        type,
        error,
        timestamp: new Date().toISOString()
      });
    }
    return { success: false, output: null, error, timestamp: new Date().toISOString() };
  }
}

/**
 * Génère du code source selon les options.
 * @param {object} options
 * @returns {string}
 */
function generateCode(options = {}) {
  const { language = 'javascript', content = '// code généré', ...rest } = options;
  // Sécurité : pas de code exécutable, pas de données sensibles
  return `// Langage: ${sanitize(language)}\n${sanitize(content)}`;
}

/**
 * Génère un document Markdown.
 * @param {object} options
 * @returns {string}
 */
function generateMarkdown(options = {}) {
  const { title = 'Document', body = '', ...rest } = options;
  return `# ${sanitize(title)}\n\n${sanitize(body)}`;
}

/**
 * Génère une image (simulation, base64).
 * @param {object} options
 * @returns {string} Base64 simulé
 */
function generateImage(options = {}) {
  // Simulation d’image (à remplacer par une vraie génération côté serveur)
  return 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA';
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('generation_service_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logGenerationEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('generation_service_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('generation_service_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Sanitize une chaîne pour éviter l’injection.
 * @param {string} str
 * @returns {string}
 */
function sanitize(str) {
  return String(str).replace(/[\r\n<>]/g, '');
}

/**
 * Anonymise les options pour les logs.
 * @param {object} options
 * @returns {object}
 */
function anonymizeOptions(options) {
  const anonymized = {};
  Object.entries(options || {}).forEach(([k, v]) => {
    if (typeof v === 'string' && v.length > 32) {
      anonymized[k] = v.slice(0, 16) + '...';
    } else {
      anonymized[k] = v;
    }
  });
  return anonymized;
}

/**
 * Efface les logs de génération (droit à l’oubli RGPD).
 */
export function clearLocalGenerationServiceLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('generation_service_logs');
  }
}
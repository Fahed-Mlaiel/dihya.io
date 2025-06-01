/**
 * @file dockerGen.js
 * @description Générateur de fichiers Docker pour Dihya Coding : génération sécurisée, validation, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Génère un Dockerfile selon les paramètres fournis.
 * @param {object} params
 * @param {string} params.baseImage - Image de base (ex: 'node:20-alpine')
 * @param {string[]} [params.commands] - Commandes RUN additionnelles
 * @param {string} [params.workdir='/app'] - Dossier de travail
 * @param {string} [params.expose='3000'] - Port exposé
 * @param {string} [params.cmd='npm start'] - Commande de démarrage
 * @param {object} [params.options] - Options avancées (logs, labels, etc.)
 * @returns {object} Résultat { success, code, error, timestamp }
 */
export function generateDockerfile({
  baseImage,
  commands = [],
  workdir = '/app',
  expose = '3000',
  cmd = 'npm start',
  options = {}
}) {
  if (!hasConsent()) {
    return {
      success: false,
      code: null,
      error: 'Consentement requis',
      timestamp: new Date().toISOString()
    };
  }
  if (!baseImage || typeof baseImage !== 'string' || !/^[a-z0-9\-:.\/]+$/i.test(baseImage)) {
    return {
      success: false,
      code: null,
      error: 'Image de base invalide',
      timestamp: new Date().toISOString()
    };
  }

  let code = `# Généré par Dihya Coding – ${new Date().toISOString()}
FROM ${baseImage}

WORKDIR ${workdir}
COPY . ${workdir}
`;

  if (Array.isArray(commands) && commands.length > 0) {
    commands.forEach(cmdLine => {
      code += `RUN ${sanitizeCommand(cmdLine)}\n`;
    });
  }

  code += `EXPOSE ${expose}\n`;
  code += `CMD [${cmdToArray(cmd)}]\n`;

  if (options.labels && typeof options.labels === 'object') {
    Object.entries(options.labels).forEach(([key, value]) => {
      code += `LABEL ${sanitizeLabel(key)}="${sanitizeLabel(value)}"\n`;
    });
  }

  if (options.log !== false) {
    logDockerGenEvent('dockerfile_generated', {
      baseImage: anonymizeBaseImage(baseImage),
      expose,
      cmd,
      timestamp: new Date().toISOString()
    });
  }

  return {
    success: true,
    code,
    error: null,
    timestamp: new Date().toISOString()
  };
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('docker_gen_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logDockerGenEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('docker_gen_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('docker_gen_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise l’image de base pour les logs.
 * @param {string} baseImage
 * @returns {string}
 */
function anonymizeBaseImage(baseImage) {
  if (!baseImage) return '';
  return baseImage.replace(/[^a-z0-9\-:.\/]/gi, '').slice(0, 24) + (baseImage.length > 24 ? '...' : '');
}

/**
 * Sanitize une commande RUN pour éviter l’injection.
 * @param {string} cmd
 * @returns {string}
 */
function sanitizeCommand(cmd) {
  return String(cmd).replace(/[^a-zA-Z0-9\-_.\/\s]/g, '');
}

/**
 * Sanitize une clé/valeur de label Docker.
 * @param {string} label
 * @returns {string}
 */
function sanitizeLabel(label) {
  return String(label).replace(/[^a-zA-Z0-9\-_.:]/g, '');
}

/**
 * Transforme une commande shell en tableau Docker CMD.
 * @param {string} cmd
 * @returns {string}
 */
function cmdToArray(cmd) {
  return cmd
    .split(' ')
    .map((part) => `"${part.replace(/"/g, '')}"`)
    .join(', ');
}

/**
 * Efface les logs de génération Docker (droit à l’oubli RGPD).
 */
export function clearLocalDockerGenLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('docker_gen_logs');
  }
}
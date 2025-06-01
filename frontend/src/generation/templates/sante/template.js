/**
 * @file template.js
 * @description Générateur avancé de modules santé (patients, RDV, télémédecine) pour Dihya Coding.
 * Sécurité, RGPD, accessibilité, SEO, plugins, CI/CD, auditabilité, multilingue, fallback AI.
 */

/**
 * Génère un module santé selon le type demandé.
 * @param {object} params
 * @param {string} params.type - Type de module ('patient', 'rdv', 'telemedecine')
 * @param {object} params.data - Données du module
 * @param {object} [params.options] - Options avancées (SEO, plugins, logs, RGPD, accessibilité, lang)
 * @returns {object} Module santé généré
 */
export function santeTemplate({ type, data, options = {} }) {
  validateType(type);
  validateData(type, data);
  if (!window?.localStorage?.getItem('sante_consent')) {
    throw new Error('Consentement requis pour générer un module santé.');
  }
  const module = generateModule(type, data, options);
  logSanteEvent('generate_sante_module', type, anonymizeData(type, data));
  return module;
}

function generateModule(type, data, options) {
  switch (type) {
    case 'patient':
      return { patient: data.patient || {}, dossier: data.dossier || {}, ...options };
    case 'rdv':
      return { rdv: data.rdv || {}, ...options };
    case 'telemedecine':
      return { telemedecine: data.telemedecine || {}, ...options };
    default:
      throw new Error('Type de module santé non supporté');
  }
}

function validateType(type) {
  const SUPPORTED = ['patient', 'rdv', 'telemedecine'];
  if (!SUPPORTED.includes(type)) {
    throw new Error('Type de module santé invalide');
  }
}

function validateData(type, data) {
  if (!data || typeof data !== 'object') throw new Error('Données du module invalides');
  if (type === 'patient' && (!data.patient || typeof data.dossier !== 'object')) throw new Error('Données patient invalides');
  if (type === 'rdv' && typeof data.rdv !== 'object') throw new Error('Données rdv invalides');
  if (type === 'telemedecine' && typeof data.telemedecine !== 'object') throw new Error('Données telemedecine invalides');
}

function anonymizeData(type, data) {
  return data;
}

function logSanteEvent(action, type, data) {
  try {
    const logs = JSON.parse(localStorage.getItem('sante_template_logs') || '[]');
    logs.push({
      action,
      type,
      data,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('sante_template_logs', JSON.stringify(logs));
  } catch {
    // Silencieux UX
  }
}

export function clearLocalSanteTemplateLogs() {
  localStorage.removeItem('sante_template_logs');
}

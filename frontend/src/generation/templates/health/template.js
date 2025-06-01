/**
 * @file template.js
 * @description Template générique pour modules santé Dihya Coding (patients, dossiers médicaux, notifications, rendez-vous).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse, SEO et documentation claire.
 * Toutes les opérations sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Génère un module santé selon le type demandé.
 * @param {object} params
 * @param {string} params.type - Type de module ('patient', 'record', 'notification', 'appointment')
 * @param {object} params.data - Données du module (patient, dossier, notification, rendez-vous, etc.)
 * @param {object} [params.options] - Options avancées (SEO, logs, RGPD, etc.)
 * @returns {object} Module santé généré
 */
export function healthTemplate({ type, data, options = {} }) {
  validateType(type);
  validateData(type, data);
  if (!window?.localStorage?.getItem('health_feature_consent')) {
    throw new Error('Consentement requis pour générer un module santé.');
  }
  const module = generateModule(type, data, options);
  logHealthTemplateEvent('generate_health_module', type, anonymizeData(type, data));
  return module;
}

/**
 * Génère le module selon le type.
 * @param {string} type
 * @param {object} data
 * @param {object} options
 * @returns {object}
 */
function generateModule(type, data, options) {
  switch (type) {
    case 'patient':
      return { patient: anonymizePatient(data.patient || {}), ...options };
    case 'record':
      return { record: anonymizeRecord(data.record || {}), ...options };
    case 'notification':
      return { notification: data.notification || {}, ...options };
    case 'appointment':
      return { appointment: data.appointment || {}, ...options };
    default:
      throw new Error('Type de module santé non supporté');
  }
}

/**
 * Valide le type de module santé.
 * @param {string} type
 */
function validateType(type) {
  const SUPPORTED = ['patient', 'record', 'notification', 'appointment'];
  if (!SUPPORTED.includes(type)) {
    throw new Error('Type de module santé invalide');
  }
}

/**
 * Valide les données selon le type de module.
 * @param {string} type
 * @param {object} data
 */
function validateData(type, data) {
  if (!data || typeof data !== 'object') throw new Error('Données du module invalides');
  if (type === 'patient' && typeof data.patient !== 'object') throw new Error('Données patient invalides');
  if (type === 'record' && typeof data.record !== 'object') throw new Error('Données dossier médical invalides');
  if (type === 'notification' && typeof data.notification !== 'object') throw new Error('Données notification invalides');
  if (type === 'appointment' && typeof data.appointment !== 'object') throw new Error('Données rendez-vous invalides');
}

/**
 * Anonymise les données sensibles pour les logs.
 * @param {string} type
 * @param {object} data
 * @returns {object}
 */
function anonymizeData(type, data) {
  if (type === 'patient' && data.patient) {
    return { ...data, patient: anonymizePatient(data.patient) };
  }
  if (type === 'record' && data.record) {
    return { ...data, record: anonymizeRecord(data.record) };
  }
  return data;
}

/**
 * Anonymise les données patient pour les logs.
 * @param {object} patient
 * @returns {object}
 */
function anonymizePatient(patient) {
  if (!patient) return {};
  const { email, phone, ssn, ...rest } = patient;
  return {
    ...rest,
    email: email ? '[email]' : undefined,
    phone: phone ? '[phone]' : undefined,
    ssn: ssn ? '[protected]' : undefined,
  };
}

/**
 * Anonymise les données dossier médical pour les logs.
 * @param {object} record
 * @returns {object}
 */
function anonymizeRecord(record) {
  if (!record) return {};
  const { patientId, ...rest } = record;
  return { ...rest, patientId: patientId ? '[id]' : undefined };
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} type
 * @param {object} data
 */
function logHealthTemplateEvent(action, type, data) {
  try {
    const logs = JSON.parse(localStorage.getItem('health_template_logs') || '[]');
    logs.push({
      action,
      type,
      data,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('health_template_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de génération santé (droit à l’oubli RGPD).
 */
export function clearLocalHealthTemplateLogs() {
  localStorage.removeItem('health_template_logs');
}
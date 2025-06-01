/**
 * @file mailService.js
 * @description Service centralisé d’envoi d’emails pour Dihya Coding : gestion des notifications, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Envoie un email de façon sécurisée et conforme RGPD.
 * @param {object} params
 * @param {string} params.to - Destinataire (email)
 * @param {string} params.subject - Sujet de l’email
 * @param {string} params.body - Corps du message (texte ou HTML)
 * @param {object} [params.options] - Options avancées (logs, cc, bcc, etc.)
 * @returns {Promise<object>} Résultat { success, error, timestamp }
 */
export async function sendMail({ to, subject, body, options = {} }) {
  if (!hasConsent()) {
    return {
      success: false,
      error: 'Consentement requis',
      timestamp: new Date().toISOString()
    };
  }
  if (!validateEmail(to)) {
    return {
      success: false,
      error: 'Adresse email invalide',
      timestamp: new Date().toISOString()
    };
  }
  if (!subject || typeof subject !== 'string' || subject.length < 2) {
    return {
      success: false,
      error: 'Sujet invalide',
      timestamp: new Date().toISOString()
    };
  }
  if (!body || typeof body !== 'string' || body.length < 2) {
    return {
      success: false,
      error: 'Corps de message invalide',
      timestamp: new Date().toISOString()
    };
  }

  // Simulation d’envoi (à remplacer par appel API sécurisé côté serveur)
  try {
    if (options.log !== false) {
      logMailEvent('send_mail', {
        to: anonymizeEmail(to),
        subject: anonymizeSubject(subject),
        timestamp: new Date().toISOString()
      });
    }
    // Simule un délai d’envoi
    await new Promise((resolve) => setTimeout(resolve, 200));
    return { success: true, error: null, timestamp: new Date().toISOString() };
  } catch (err) {
    if (options.log !== false) {
      logMailEvent('send_mail_error', {
        to: anonymizeEmail(to),
        subject: anonymizeSubject(subject),
        error: err.message,
        timestamp: new Date().toISOString()
      });
    }
    return { success: false, error: err.message, timestamp: new Date().toISOString() };
  }
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('mail_service_feature_consent');
}

/**
 * Valide une adresse email.
 * @param {string} email
 * @returns {boolean}
 */
function validateEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logMailEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('mail_service_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('mail_service_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise une adresse email pour les logs.
 * @param {string} email
 * @returns {string}
 */
function anonymizeEmail(email) {
  if (typeof email !== 'string') return '';
  const [user, domain] = email.split('@');
  return user ? user[0] + '***@' + (domain || '') : '[email]';
}

/**
 * Anonymise un sujet pour les logs.
 * @param {string} subject
 * @returns {string}
 */
function anonymizeSubject(subject) {
  if (!subject) return '';
  return subject.length > 16 ? subject.slice(0, 8) + '...' : subject;
}

/**
 * Efface les logs d’emails (droit à l’oubli RGPD).
 */
export function clearLocalMailServiceLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('mail_service_logs');
  }
}
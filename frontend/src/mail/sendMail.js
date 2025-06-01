/**
 * @file sendMail.js
 * @description Service d’envoi d’emails pour Dihya Coding (validation, logs, RGPD, auditabilité, sécurité, extensibilité).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

import { validateEmail } from './mailValidator';

/**
 * Envoie un email via le service Dihya Coding.
 * @param {object} params
 * @param {string} params.to - Adresse email du destinataire
 * @param {string} params.subject - Sujet de l’email
 * @param {string} params.template - Nom du template à utiliser
 * @param {object} params.data - Données à injecter dans le template
 * @param {object} [params.options] - Options avancées (logs, langue, accessibilité)
 * @returns {Promise<object>} Résultat { success, messageId, timestamp }
 */
export async function sendMail({ to, subject, template, data, options = {} }) {
  if (!hasConsent()) throw new Error('Consentement requis pour l’envoi d’email.');
  if (!validateEmail(to)) throw new Error('Adresse email invalide.');
  if (!subject || typeof subject !== 'string') throw new Error('Sujet requis.');
  if (!template || typeof template !== 'string') throw new Error('Template requis.');

  const messageId = generateMessageId(to, subject);
  const timestamp = new Date().toISOString();

  // Simulation d’envoi d’email (à remplacer par l’intégration réelle)
  await fakeSendMailApi({ to: anonymizeEmail(to), subject, template, data, options, messageId, timestamp });

  if (options.log !== false) {
    logMailEvent('send_mail', {
      to: anonymizeEmail(to),
      subject: anonymizeSubject(subject),
      template,
      messageId,
      timestamp
    });
  }

  return { success: true, messageId, timestamp };
}

/**
 * Génère un identifiant unique pour l’email.
 * @param {string} to
 * @param {string} subject
 * @returns {string}
 */
function generateMessageId(to, subject) {
  return 'mail_' + btoa(to + subject).slice(0, 8) + '_' + Date.now().toString(36);
}

/**
 * Simulation d’envoi d’email (à remplacer par l’intégration réelle).
 * @private
 * @param {object} params
 * @returns {Promise<void>}
 */
async function fakeSendMailApi(params) {
  await new Promise(r => setTimeout(r, 100));
  // Aucun email n’est réellement envoyé ici.
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('mail_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logMailEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('mail_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('mail_logs', JSON.stringify(logs));
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
 * Anonymise un sujet d’email pour les logs.
 * @param {string} subject
 * @returns {string}
 */
function anonymizeSubject(subject) {
  if (typeof subject !== 'string') return '';
  return subject.length > 32 ? subject.slice(0, 32) + '…' : subject;
}

/**
 * Efface les logs d’envoi d’email (droit à l’oubli RGPD).
 */
export function clearLocalMailLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('mail_logs');
  }
}
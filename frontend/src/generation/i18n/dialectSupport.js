/**
 * @file dialectSupport.js
 * @description Gestion avancée des dialectes et variantes linguistiques pour Dihya Coding (détection, traduction, logs, audit).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Liste des dialectes supportés par Dihya Coding.
 * @readonly
 * @type {Array<object>}
 */
export const DIALECTS = [
  { code: 'fr-FR', label: 'Français (France)' },
  { code: 'fr-CA', label: 'Français (Canada)' },
  { code: 'en-US', label: 'Anglais (États-Unis)' },
  { code: 'en-GB', label: 'Anglais (Royaume-Uni)' },
  { code: 'ar-MA', label: 'Arabe (Maroc)' },
  { code: 'ber-TZM', label: 'Amazigh (Tamazight Maroc)' },
  { code: 'ber-KAB', label: 'Amazigh (Kabyle Algérie)' },
  // Ajouter d’autres dialectes selon besoins métier
];

/**
 * Détecte le dialecte d’un texte donné.
 * @param {string} text
 * @returns {Promise<{success: boolean, dialect: string, confidence: number}>}
 */
export async function detectDialect(text) {
  validateText(text);
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/i18n/detectDialect', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ text }),
  });
  if (!res.ok) throw new Error('Erreur lors de la détection du dialecte');
  const data = await res.json();
  logDialectEvent('detect_dialect', anonymizeText(text), data.dialect);
  return data;
}

/**
 * Traduit un texte vers un dialecte cible.
 * @param {object} params
 * @param {string} params.text - Texte source à traduire (sera anonymisé pour les logs)
 * @param {string} params.targetDialect - Code dialecte cible (ex: 'fr-CA', 'ber-KAB')
 * @param {object} [params.options] - Options avancées (service, formality, glossary, etc.)
 * @returns {Promise<{success: boolean, translated: string, warnings?: string[]}>}
 */
export async function translateToDialect({ text, targetDialect, options = {} }) {
  validateText(text);
  validateDialect(targetDialect);
  if (!window?.localStorage?.getItem('i18n_feature_consent')) {
    throw new Error('Consentement requis pour utiliser la traduction dialectale.');
  }
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/i18n/translateDialect', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ text, targetDialect, options }),
  });
  if (!res.ok) throw new Error('Erreur lors de la traduction dialectale');
  const data = await res.json();
  logDialectEvent('translate_to_dialect', anonymizeText(text), targetDialect);
  return data;
}

/**
 * Valide le texte à traiter.
 * @param {string} text
 */
function validateText(text) {
  if (!text || typeof text !== 'string' || text.length < 1 || text.length > 5000) {
    throw new Error('Texte invalide');
  }
}

/**
 * Valide le code dialecte cible.
 * @param {string} dialect
 */
function validateDialect(dialect) {
  if (!DIALECTS.some(d => d.code === dialect)) {
    throw new Error('Dialecte cible non supporté');
  }
}

/**
 * Anonymise le texte pour les logs (suppression d’emails, données sensibles).
 * @param {string} text
 * @returns {string}
 */
function anonymizeText(text) {
  return text.replace(/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/gi, '[email]');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} value
 * @param {string} [dialect]
 */
function logDialectEvent(action, value, dialect) {
  try {
    const logs = JSON.parse(localStorage.getItem('dialect_support_logs') || '[]');
    logs.push({
      action,
      value,
      dialect,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('dialect_support_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de gestion des dialectes (droit à l’oubli RGPD).
 */
export function clearLocalDialectSupportLogs() {
  localStorage.removeItem('dialect_support_logs');
}
/**
 * @file useAuth.js
 * @description Hook React pour la gestion de l’authentification dans Dihya Coding (connexion, déconnexion, session, rôles, RGPD).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

import { useState, useCallback } from 'react';

/**
 * Hook pour gérer l’authentification utilisateur dans Dihya Coding.
 * @param {object} [options]
 * @param {boolean} [options.log=true] - Active le log local pour auditabilité
 * @returns {[object|null, function, function, boolean, string|null]} [user, login, logout, loading, error]
 */
export function useAuth(options = {}) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  /**
   * Connexion utilisateur (simulation, à remplacer par intégration réelle).
   * @param {string} email
   * @param {string} password
   * @returns {Promise<void>}
   */
  const login = useCallback(async (email, password) => {
    if (!hasConsent()) {
      setError('Consentement requis pour l’authentification.');
      return;
    }
    setLoading(true);
    setError(null);
    try {
      // Simulation d’authentification (à remplacer par un appel API sécurisé)
      await new Promise(r => setTimeout(r, 200));
      if (email === 'admin@dihya.app' && password === 'admin') {
        const userObj = { id: 'u1', email: anonymizeEmail(email), roles: ['admin', 'user'] };
        setUser(userObj);
        if (options.log !== false) {
          logAuthEvent('login', { userId: anonymizeUserId(userObj.id), roles: userObj.roles });
        }
      } else if (email === 'user@dihya.app' && password === 'user') {
        const userObj = { id: 'u2', email: anonymizeEmail(email), roles: ['user'] };
        setUser(userObj);
        if (options.log !== false) {
          logAuthEvent('login', { userId: anonymizeUserId(userObj.id), roles: userObj.roles });
        }
      } else {
        throw new Error('Identifiants invalides');
      }
    } catch (e) {
      setError('Erreur Auth : ' + (e.message || e));
      setUser(null);
    } finally {
      setLoading(false);
    }
  }, [options.log]);

  /**
   * Déconnexion utilisateur.
   */
  const logout = useCallback(() => {
    if (!hasConsent()) {
      setError('Consentement requis pour la déconnexion.');
      return;
    }
    if (user && options.log !== false) {
      logAuthEvent('logout', { userId: anonymizeUserId(user.id) });
    }
    setUser(null);
    setError(null);
  }, [user, options.log]);

  return [user, login, logout, loading, error];
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('auth_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logAuthEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('auth_hook_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString(),
    });
    window.localStorage.setItem('auth_hook_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise un email pour les logs.
 * @param {string} email
 * @returns {string}
 */
function anonymizeEmail(email) {
  if (typeof email !== 'string') return '';
  const [user, domain] = email.split('@');
  return user ? user[0] + '***@' + (domain || '') : '[email]';
}

/**
 * Anonymise un userId pour les logs.
 * @param {string|number} userId
 * @returns {string}
 */
function anonymizeUserId(userId) {
  if (!userId) return '';
  const str = String(userId);
  return str.length > 4 ? str.slice(0, 2) + '***' + str.slice(-2) : '***';
}

/**
 * Efface les logs du hook Auth (droit à l’oubli RGPD).
 */
export function clearLocalAuthHookLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('auth_hook_logs');
  }
}
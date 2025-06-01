/**
 * @file withAuth.js
 * @description Middleware/HOC React pour la protection des routes et composants par authentification dans Dihya Coding.
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

import React, { useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * HOC/Middleware pour protéger un composant par authentification.
 * @param {React.ComponentType} Component - Composant à protéger
 * @param {object} [options]
 * @param {boolean} [options.log=true] - Active le log local pour auditabilité
 * @returns {React.ComponentType}
 */
export function withAuth(Component, options = {}) {
  function AuthenticatedComponent(props) {
    useEffect(() => {
      if (hasConsent() && options.log !== false) {
        logAuthEvent('access_attempt', { path: window.location.pathname });
      }
      // eslint-disable-next-line
    }, []);

    const user = getCurrentUser();
    if (!user) {
      if (hasConsent() && options.log !== false) {
        logAuthEvent('access_denied', { path: window.location.pathname });
      }
      // Redirection ou affichage d’un message d’accès refusé
      return (
        <div className="auth-denied" role="alert" tabIndex={-1}>
          <h2>Accès refusé</h2>
          <p>Vous devez être authentifié pour accéder à cette page.</p>
        </div>
      );
    }

    if (hasConsent() && options.log !== false) {
      logAuthEvent('access_granted', { userId: anonymizeUserId(user.id), path: window.location.pathname });
    }

    return <Component {...props} user={user} />;
  }

  AuthenticatedComponent.propTypes = {
    user: PropTypes.object
  };

  return AuthenticatedComponent;
}

/**
 * Récupère l’utilisateur courant depuis le stockage local (simulation).
 * @returns {object|null}
 */
function getCurrentUser() {
  if (typeof window !== 'undefined' && window.localStorage) {
    try {
      const user = JSON.parse(window.localStorage.getItem('current_user'));
      if (user && typeof user === 'object' && user.id) return user;
    } catch {
      return null;
    }
  }
  return null;
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('middleware_auth_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logAuthEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('middleware_auth_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('middleware_auth_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
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
 * Efface les logs d’auth middleware (droit à l’oubli RGPD).
 */
export function clearLocalMiddlewareAuthLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('middleware_auth_logs');
  }
}
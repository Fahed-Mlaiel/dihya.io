/**
 * @file withRole.js
 * @description Middleware/HOC React pour la gestion des rôles et permissions dans Dihya Coding (sécurité, RGPD, auditabilité, extensibilité).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

import React, { useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * HOC/Middleware pour protéger un composant selon le rôle utilisateur.
 * @param {React.ComponentType} Component - Composant à protéger
 * @param {string[]} allowedRoles - Rôles autorisés (ex: ['admin', 'editor'])
 * @param {object} [options]
 * @param {boolean} [options.log=true] - Active le log local pour auditabilité
 * @returns {React.ComponentType}
 */
export function withRole(Component, allowedRoles = [], options = {}) {
  function RoleProtectedComponent(props) {
    useEffect(() => {
      if (hasConsent() && options.log !== false) {
        logRoleEvent('role_access_attempt', {
          path: window.location.pathname,
          allowedRoles
        });
      }
      // eslint-disable-next-line
    }, []);

    const user = getCurrentUser();
    const hasRole = user && allowedRoles.includes(user.role);

    if (!user || !hasRole) {
      if (hasConsent() && options.log !== false) {
        logRoleEvent('role_access_denied', {
          path: window.location.pathname,
          userId: user ? anonymizeUserId(user.id) : null,
          userRole: user ? user.role : null,
          allowedRoles
        });
      }
      // Affichage d’un message d’accès refusé
      return (
        <div className="role-denied" role="alert" tabIndex={-1}>
          <h2>Accès refusé</h2>
          <p>Vous n’avez pas les permissions nécessaires pour accéder à cette page.</p>
        </div>
      );
    }

    if (hasConsent() && options.log !== false) {
      logRoleEvent('role_access_granted', {
        userId: anonymizeUserId(user.id),
        userRole: user.role,
        path: window.location.pathname
      });
    }

    return <Component {...props} user={user} />;
  }

  RoleProtectedComponent.propTypes = {
    user: PropTypes.object
  };

  return RoleProtectedComponent;
}

/**
 * Récupère l’utilisateur courant depuis le stockage local (simulation).
 * @returns {object|null}
 */
function getCurrentUser() {
  if (typeof window !== 'undefined' && window.localStorage) {
    try {
      const user = JSON.parse(window.localStorage.getItem('current_user'));
      if (user && typeof user === 'object' && user.id && user.role) return user;
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
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('middleware_role_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logRoleEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('middleware_role_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('middleware_role_logs', JSON.stringify(logs));
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
 * Efface les logs de rôle middleware (droit à l’oubli RGPD).
 */
export function clearLocalMiddlewareRoleLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('middleware_role_logs');
  }
}
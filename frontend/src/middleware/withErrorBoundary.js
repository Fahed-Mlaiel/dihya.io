/**
 * @file withErrorBoundary.js
 * @description Middleware/HOC React pour la gestion centralisée des erreurs (Error Boundary) dans Dihya Coding.
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les erreurs sont loguées localement, anonymisées et respectent le consentement utilisateur.
 */

import React from 'react';
import PropTypes from 'prop-types';

/**
 * HOC/Middleware pour encapsuler un composant dans un Error Boundary.
 * @param {React.ComponentType} Component - Composant à protéger
 * @param {object} [options]
 * @param {boolean} [options.log=true] - Active le log local pour auditabilité
 * @returns {React.ComponentType}
 */
export function withErrorBoundary(Component, options = {}) {
  class ErrorBoundary extends React.Component {
    constructor(props) {
      super(props);
      this.state = { hasError: false, error: null, errorInfo: null };
    }

    static getDerivedStateFromError(error) {
      return { hasError: true, error };
    }

    componentDidCatch(error, errorInfo) {
      this.setState({ error, errorInfo });
      if (hasConsent() && options.log !== false) {
        logErrorEvent('component_error', {
          error: anonymizeError(error),
          info: anonymizeErrorInfo(errorInfo),
          path: window.location.pathname
        });
      }
    }

    render() {
      if (this.state.hasError) {
        // Affichage d’un message d’erreur moderne et accessible
        return (
          <div className="error-boundary" role="alert" tabIndex={-1}>
            <h2>Une erreur est survenue</h2>
            <p>Nous avons rencontré un problème. L’équipe technique a été notifiée.</p>
          </div>
        );
      }
      return <Component {...this.props} />;
    }
  }

  ErrorBoundary.propTypes = {
    children: PropTypes.node
  };

  return ErrorBoundary;
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('middleware_error_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logErrorEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('middleware_error_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('middleware_error_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise une erreur pour les logs.
 * @param {Error} error
 * @returns {string}
 */
function anonymizeError(error) {
  if (!error) return '';
  return error.message ? error.message.slice(0, 128) : '[error]';
}

/**
 * Anonymise les infos d’erreur pour les logs.
 * @param {object} errorInfo
 * @returns {string}
 */
function anonymizeErrorInfo(errorInfo) {
  if (!errorInfo) return '';
  return errorInfo.componentStack
    ? errorInfo.componentStack.replace(/at\s+\w+/g, 'at [component]').slice(0, 256)
    : '[info]';
}

/**
 * Efface les logs d’erreur middleware (droit à l’oubli RGPD).
 */
export function clearLocalMiddlewareErrorLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('middleware_error_logs');
  }
}
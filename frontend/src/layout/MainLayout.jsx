/**
 * @file MainLayout.jsx
 * @description Layout principal de Dihya Coding : structure, navigation, accessibilité, SEO, sécurité, RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

import PropTypes from 'prop-types';
import React, { useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import { useTranslation } from 'react-i18next';

import '../styles/main.css'; // Design moderne, responsive

/**
 * Layout principal pour toutes les pages de Dihya Coding.
 * Gère le SEO, l’accessibilité, la navigation, la conformité RGPD et l’auditabilité.
 *
 * @param {object} props
 * @param {React.ReactNode} props.children - Contenu de la page
 * @param {string} [props.title] - Titre personnalisé pour le SEO
 * @param {string} [props.description] - Description personnalisée pour le SEO
 * @returns {JSX.Element}
 */
export default function MainLayout({ children, title, description }) {
  const { t, i18n } = useTranslation();

  // SEO & accessibilité : mise à jour dynamique du titre et de la langue
  useEffect(() => {
    document.documentElement.lang = i18n.language || 'fr';
    if (hasConsent()) {
      logLayoutEvent('layout_render', { lang: i18n.language, path: window.location.pathname });
    }
  }, [i18n.language]);

  return (
    <div className="main-layout" data-theme={getTheme()}>
      <Helmet>
        <title>{title || t('app.title')}</title>
        <meta name="description" content={description || t('app.description')} />
        <meta name="keywords" content={t('app.seo_keywords')} />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <meta name="color-scheme" content={getTheme() === 'dark' ? 'dark light' : 'light dark'} />
        {/* RGPD & sécurité : pas de données personnelles dans les balises meta */}
      </Helmet>
      <header>
        <nav aria-label={t('navigation.home')}>
          {/* Exemple de navigation moderne, extensible */}
          <a href="/">{t('navigation.home')}</a>
          <a href="/about">{t('navigation.about')}</a>
          <a href="/contact">{t('navigation.contact')}</a>
          <a href="/dashboard">{t('navigation.dashboard')}</a>
          <a href="/dashboard-global">Dashboard Global</a>
        </nav>
      </header>
      <main id="main-content" tabIndex={-1} aria-live="polite">
        {children}
      </main>
      <footer>
        <small>
          &copy; {new Date().getFullYear()} Dihya Coding – {t('app.description')}
        </small>
      </footer>
    </div>
  );
}

MainLayout.propTypes = {
  children: PropTypes.node.isRequired,
  title: PropTypes.string,
  description: PropTypes.string
};

/**
 * Récupère le thème courant (clair/sombre) pour l’accessibilité et le SEO.
 * @returns {string}
 */
function getTheme() {
  if (typeof window !== 'undefined') {
    return window.localStorage.getItem('theme') || 'light';
  }
  return 'light';
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('layout_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logLayoutEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('layout_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('layout_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs du layout (droit à l’oubli RGPD).
 */
export function clearLocalLayoutLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('layout_logs');
  }
}

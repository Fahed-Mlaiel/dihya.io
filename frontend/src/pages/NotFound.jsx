/**
 * @file NotFound.jsx
 * @description Page 404 pour Dihya Coding : design moderne, SEO, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

import React, { useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import MainLayout from '../layout/MainLayout';
import { Sparkles, AlertTriangle } from "lucide-react";

/**
 * Page d’erreur 404 (non trouvée).
 * @returns {JSX.Element}
 */
export default function NotFound() {
  const { t, i18n } = useTranslation();

  useEffect(() => {
    if (hasConsent()) {
      logNotFoundEvent('not_found_view', { lang: i18n.language, path: window.location.pathname });
    }
  }, [i18n.language]);

  return (
    <MainLayout title={t('notfound.title')} description={t('notfound.description')}>
      <section className="w-full max-w-lg mx-auto bg-white/90 rounded-xl shadow-lg p-10 mt-16 mb-16 border border-gray-100 flex flex-col items-center" aria-labelledby="notfound-title">
        <div className="flex items-center gap-3 mb-4">
          <AlertTriangle className="w-10 h-10 text-yellow-500" />
          <h1 id="notfound-title" className="text-3xl font-bold text-gray-900 tracking-wide">
            {t('notfound.title') || '404 – Page non trouvée'}
          </h1>
        </div>
        <p className="text-lg text-gray-700 mb-6 text-center max-w-md">
          {t('notfound.description') || 'La page demandée est introuvable ou a été déplacée.'}
        </p>
        <a
          href="/"
          className="cta-btn px-8 py-3 rounded-lg bg-yellow-400 hover:bg-yellow-500 text-gray-900 font-bold text-lg shadow transition mb-2"
        >
          {t('navigation.home') || 'Retour à l’accueil'}
        </a>
        <div className="mt-6 text-xs text-gray-400 text-center">
          <span>
            <a href="https://github.com/DihyaCoding/templates" target="_blank" rel="noopener noreferrer" className="underline hover:text-yellow-600">
              Voir des exemples de templates métiers
            </a>
            {" • "}
            <a href="/docs/contributing" className="underline hover:text-yellow-600">
              Contribuer
            </a>
          </span>
        </div>
        <footer className="mt-10 text-center text-xs text-gray-400">
          <span>
            Slogan : <i>De l’idée au code, en toute souveraineté.</i>
          </span>
        </footer>
      </section>
    </MainLayout>
  );
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('notfound_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logNotFoundEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('notfound_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('notfound_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs notfound (droit à l’oubli RGPD).
 */
export function clearLocalNotFoundLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('notfound_logs');
  }
}
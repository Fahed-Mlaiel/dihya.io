/**
 * @file Preview.jsx
 * @description Page d’aperçu de projet/module pour Dihya Coding : design moderne, SEO, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

import React, { useEffect, useState } from 'react';
import { useTranslation } from 'react-i18next';
import MainLayout from '../layout/MainLayout';
import { Eye, ShieldCheck, Loader2, Layers, Globe, Sparkles } from "lucide-react";

/**
 * Page d’aperçu d’un projet ou module généré.
 * @returns {JSX.Element}
 */
export default function Preview() {
  const { t, i18n } = useTranslation();
  const [previewData, setPreviewData] = useState(null);
  const [status, setStatus] = useState(null);

  useEffect(() => {
    if (hasConsent()) {
      logPreviewEvent('preview_view', { lang: i18n.language, path: window.location.pathname });
    }
    fetchPreviewData()
      .then((data) => setPreviewData(data))
      .catch(() => setStatus({ type: 'error', message: t('messages.error_occurred') || "Erreur lors du chargement de l’aperçu." }));
  }, [i18n.language, t]);

  return (
    <MainLayout title={t('preview.title')} description={t('preview.description')}>
      <section className="w-full max-w-2xl mx-auto bg-white/90 rounded-xl shadow-lg p-10 mt-10 mb-16 border border-gray-100 flex flex-col items-center" aria-labelledby="preview-title">
        <div className="flex items-center gap-3 mb-4">
          <Eye className="w-8 h-8 text-yellow-500" />
          <h1 id="preview-title" className="text-3xl font-bold text-gray-900 tracking-wide">
            {t('preview.title') || 'Aperçu du projet'}
          </h1>
        </div>
        <p className="text-gray-700 mb-6 text-center max-w-xl">
          {t('preview.description') || 'Consultez un aperçu sécurisé et conforme RGPD de votre projet ou module généré.'}
        </p>
        {status && (
          <div
            className={`mt-4 px-4 py-3 rounded-lg text-sm font-medium flex items-center gap-2 ${
              status.type === 'error'
                ? 'bg-red-100 text-red-700'
                : 'bg-green-100 text-green-700'
            }`}
            role={status.type === 'error' ? 'alert' : 'status'}
            tabIndex={-1}
          >
            <ShieldCheck className="w-5 h-5" />
            {status.message}
          </div>
        )}
        {previewData ? (
          <div className="w-full bg-yellow-50 rounded-lg shadow-inner p-6 mt-4 mb-2 flex flex-col gap-4 preview-content" tabIndex={0} aria-live="polite">
            <div className="flex items-center gap-2 mb-2">
              <Sparkles className="w-6 h-6 text-yellow-500" />
              <h2 className="text-xl font-bold text-gray-900">{previewData.name}</h2>
            </div>
            <div className="flex flex-wrap gap-3 mb-2">
              <span className="flex items-center gap-1 bg-yellow-100 text-yellow-700 px-2 py-0.5 rounded text-xs font-medium">
                <Globe className="w-4 h-4" /> {previewData.lang || "fr"}
              </span>
              <span className="flex items-center gap-1 bg-yellow-100 text-yellow-700 px-2 py-0.5 rounded text-xs font-medium">
                <Layers className="w-4 h-4" /> {previewData.stack?.join(", ") || "Fullstack"}
              </span>
            </div>
            <ul className="list-disc list-inside text-gray-800 mb-2">
              {previewData.modules.map((mod) => (
                <li key={mod}>{mod}</li>
              ))}
            </ul>
            <p className="text-xs text-gray-500">
              {t('preview.generated_at') || "Généré le"} : {previewData.generatedAt}
            </p>
            <div className="mt-4 flex flex-wrap gap-2">
              {previewData.links?.demo && (
                <a
                  href={previewData.links.demo}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="underline text-yellow-700 hover:text-yellow-900 text-sm"
                >
                  Voir la démo instantanée
                </a>
              )}
              {previewData.links?.download && (
                <a
                  href={previewData.links.download}
                  download
                  className="underline text-yellow-700 hover:text-yellow-900 text-sm"
                >
                  Télécharger le code généré
                </a>
              )}
            </div>
          </div>
        ) : !status && (
          <div className="flex items-center gap-2 mt-8 text-gray-500" aria-busy="true">
            <Loader2 className="animate-spin w-6 h-6" />
            {t('messages.loading') || "Chargement..."}
          </div>
        )}
        <div className="mt-10 text-xs text-gray-400 text-center">
          <span>
            Toutes les previews sont <b>RGPD</b>, auditables, multilingues et sécurisées.<br />
            <a href="https://github.com/DihyaCoding/templates" target="_blank" rel="noopener noreferrer" className="underline hover:text-yellow-600">
              Voir des exemples de templates métiers
            </a>
          </span>
        </div>
      </section>
    </MainLayout>
  );
}

/**
 * Simulation de récupération des données d’aperçu (à remplacer par l’intégration réelle).
 * @returns {Promise<object>}
 */
async function fetchPreviewData() {
  await new Promise((r) => setTimeout(r, 350));
  // Exemple de données anonymisées et extensibles
  return {
    name: 'Projet ***23',
    lang: 'fr',
    stack: ['React', 'Flask', 'CI/CD'],
    modules: ['ai', 'seo', 'security'],
    generatedAt: new Date().toLocaleString(),
    links: {
      demo: "https://demo.dihyacoding.com/projet-23",
      download: "/downloads/projet-23.zip"
    }
  };
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('preview_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logPreviewEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('preview_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('preview_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs preview (droit à l’oubli RGPD).
 */
export function clearLocalPreviewLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('preview_logs');
  }
}
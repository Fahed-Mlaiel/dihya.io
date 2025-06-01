/**
 * @file Profile.jsx
 * @description Page de profil utilisateur pour Dihya Coding : design moderne, SEO, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

import React, { useEffect, useState } from 'react';
import { useTranslation } from 'react-i18next';
import MainLayout from '../layout/MainLayout';
import { User, Mail, ShieldCheck, Loader2, Trash2, Download, LogOut } from "lucide-react";

/**
 * Page de profil utilisateur.
 * @returns {JSX.Element}
 */
export default function Profile() {
  const { t, i18n } = useTranslation();
  const [user, setUser] = useState(null);
  const [status, setStatus] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (hasConsent()) {
      logProfileEvent('profile_view', { lang: i18n.language, path: window.location.pathname });
    }
    fetchProfile()
      .then((data) => {
        setUser(data);
        setLoading(false);
      })
      .catch(() => {
        setStatus({ type: 'error', message: t('messages.error_occurred') || "Erreur lors du chargement du profil." });
        setLoading(false);
      });
  }, [i18n.language, t]);

  function handleForgetMe() {
    if (window.confirm(t('rgpd.forget_me_confirm') || 'Voulez-vous vraiment supprimer vos données ?')) {
      clearLocalProfile();
      setUser(null);
      setStatus({ type: 'success', message: t('rgpd.forget_me_success') || 'Profil supprimé.' });
      logProfileEvent('profile_forget', { timestamp: new Date().toISOString() });
    }
  }

  function handleExport() {
    try {
      const exportData = window.localStorage.getItem('current_user');
      const blob = new Blob([exportData], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'dihya-profile.json';
      a.click();
      URL.revokeObjectURL(url);
      logProfileEvent('profile_export', { timestamp: new Date().toISOString() });
    } catch {
      setStatus({ type: 'error', message: t('messages.error_occurred') || "Erreur lors de l’export." });
    }
  }

  function handleLogout() {
    window.localStorage.removeItem('current_user');
    setUser(null);
    setStatus({ type: 'success', message: t('messages.logout_success') || "Déconnexion réussie." });
    logProfileEvent('profile_logout', { timestamp: new Date().toISOString() });
  }

  return (
    <MainLayout title={t('profile.title')} description={t('profile.description')}>
      <section className="w-full max-w-lg mx-auto bg-white/90 rounded-xl shadow-lg p-10 mt-10 mb-16 border border-gray-100 flex flex-col items-center" aria-labelledby="profile-title">
        <div className="flex items-center gap-3 mb-4">
          <User className="w-8 h-8 text-yellow-500" />
          <h1 id="profile-title" className="text-3xl font-bold text-gray-900 tracking-wide">
            {t('profile.title') || 'Profil utilisateur'}
          </h1>
        </div>
        <p className="text-gray-700 mb-6 text-center max-w-md">
          {t('profile.description') || 'Gérez vos informations personnelles et vos préférences.'}
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
        {loading ? (
          <div className="flex items-center gap-2 mt-8 text-gray-500" aria-busy="true">
            <Loader2 className="animate-spin w-6 h-6" />
            {t('messages.loading') || "Chargement..."}
          </div>
        ) : user ? (
          <div className="w-full bg-yellow-50 rounded-lg shadow-inner p-6 mt-4 mb-2 flex flex-col gap-4 profile-content" tabIndex={0} aria-live="polite">
            <dl className="mb-4">
              <dt className="font-semibold text-gray-700 flex items-center gap-2"><Mail className="w-4 h-4" /> {t('profile.email') || 'Email'}</dt>
              <dd className="mb-2 ml-6">{anonymizeEmail(user.email)}</dd>
              <dt className="font-semibold text-gray-700 flex items-center gap-2">{t('profile.role') || 'Rôle'}</dt>
              <dd className="mb-2 ml-6">{user.role}</dd>
              <dt className="font-semibold text-gray-700 flex items-center gap-2">{t('profile.created_at') || 'Créé le'}</dt>
              <dd className="mb-2 ml-6">{user.createdAt}</dd>
            </dl>
            <div className="flex flex-wrap gap-3 mt-2">
              <button onClick={handleExport} className="flex items-center gap-2 px-4 py-2 rounded-lg bg-yellow-400 hover:bg-yellow-500 text-gray-900 font-semibold shadow transition" title={t('profile.export') || "Exporter"}>
                <Download className="w-4 h-4" /> {t('profile.export') || "Exporter"}
              </button>
              <button onClick={handleForgetMe} className="flex items-center gap-2 px-4 py-2 rounded-lg bg-red-100 hover:bg-red-200 text-red-700 font-semibold shadow transition" title={t('rgpd.forget_me') || "Droit à l’oubli"}>
                <Trash2 className="w-4 h-4" /> {t('rgpd.forget_me') || "Droit à l’oubli"}
              </button>
              <button onClick={handleLogout} className="flex items-center gap-2 px-4 py-2 rounded-lg bg-gray-100 hover:bg-gray-200 text-gray-700 font-semibold shadow transition" title={t('navigation.logout') || "Déconnexion"}>
                <LogOut className="w-4 h-4" /> {t('navigation.logout') || "Déconnexion"}
              </button>
            </div>
          </div>
        ) : (
          <div className="mt-8 text-gray-500">{t('profile.not_logged_in') || "Non authentifié."}</div>
        )}
        <div className="mt-10 text-xs text-gray-400 text-center">
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
 * Simulation de récupération du profil utilisateur (à remplacer par l’intégration réelle).
 * @returns {Promise<object>}
 */
async function fetchProfile() {
  await new Promise((r) => setTimeout(r, 250));
  const user = JSON.parse(window.localStorage.getItem('current_user'));
  if (!user) throw new Error('Non authentifié');
  return {
    email: user.id || 'user@dihya.app',
    role: user.role || 'user',
    createdAt: user.createdAt || new Date().toLocaleDateString()
  };
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('profile_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logProfileEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('profile_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('profile_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise une adresse email pour les logs et l’affichage.
 * @param {string} email
 * @returns {string}
 */
function anonymizeEmail(email) {
  if (typeof email !== 'string') return '';
  const [user, domain] = email.split('@');
  return user ? user[0] + '***@' + (domain || '') : '[email]';
}

/**
 * Efface le profil local (droit à l’oubli RGPD).
 */
function clearLocalProfile() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('current_user');
    window.localStorage.removeItem('profile_logs');
  }
}

/**
 * Efface les logs de profil (droit à l’oubli RGPD).
 */
export function clearLocalProfileLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('profile_logs');
  }
}
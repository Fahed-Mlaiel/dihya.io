/**
 * @file Login.jsx
 * @description Page de connexion pour Dihya Coding : design moderne, sécurité, RGPD, auditabilité, accessibilité, extensibilité.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

import React, { useState } from 'react';
import { useTranslation } from 'react-i18next';
import MainLayout from '../layout/MainLayout';
import { ShieldCheck, User, Lock, Loader2 } from "lucide-react";

/**
 * Page de connexion utilisateur.
 * @returns {JSX.Element}
 */
export default function Login() {
  const { t } = useTranslation();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [status, setStatus] = useState(null);
  const [loading, setLoading] = useState(false);

  /**
   * Gère la soumission du formulaire de connexion.
   * @param {React.FormEvent} e
   */
  const handleSubmit = async (e) => {
    e.preventDefault();
    setStatus(null);

    if (!hasConsent()) {
      setStatus({ type: 'error', message: t('rgpd.consent_required') || "Consentement RGPD requis." });
      return;
    }
    if (!validateEmail(email)) {
      setStatus({ type: 'error', message: t('forms.invalid_email') || "Email invalide." });
      return;
    }
    if (!password || password.length < 6) {
      setStatus({ type: 'error', message: t('forms.required') || "Mot de passe requis (6 caractères min)." });
      return;
    }

    try {
      setLoading(true);
      await fakeLogin({ email, password });
      logLoginEvent('login_success', {
        email: anonymizeEmail(email),
        timestamp: new Date().toISOString()
      });
      window.localStorage.setItem('current_user', JSON.stringify({ id: email, role: 'user' }));
      setStatus({ type: 'success', message: t('messages.login_success') || "Connexion réussie !" });
      setEmail('');
      setPassword('');
      // Redirection possible ici
    } catch (err) {
      logLoginEvent('login_error', {
        email: anonymizeEmail(email),
        error: err.message,
        timestamp: new Date().toISOString()
      });
      setStatus({ type: 'error', message: t('messages.error_occurred') || "Erreur lors de la connexion." });
    } finally {
      setLoading(false);
    }
  };

  return (
    <MainLayout title={t('navigation.login')} description={t('app.description')}>
      <section className="w-full max-w-md mx-auto bg-white/90 rounded-xl shadow-lg p-8 mt-12 mb-16 border border-gray-100 flex flex-col items-center" aria-labelledby="login-title">
        <div className="flex items-center gap-3 mb-4">
          <ShieldCheck className="w-8 h-8 text-yellow-500" />
          <h1 id="login-title" className="text-2xl font-bold text-gray-900 tracking-wide">
            {t('navigation.login') || "Connexion"}
          </h1>
        </div>
        <form onSubmit={handleSubmit} aria-describedby="login-desc" className="w-full flex flex-col gap-5">
          <div id="login-desc" className="sr-only">
            {t('app.description')}
          </div>
          <label htmlFor="email" className="font-semibold text-gray-700 flex items-center gap-2">
            <User className="w-4 h-4 text-yellow-500" />
            {t('forms.email') || "Email"}
          </label>
          <input
            id="email"
            name="email"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            autoComplete="username"
            aria-required="true"
            className="w-full px-4 py-2 rounded-lg border border-gray-200 focus:border-yellow-400 focus:ring-2 focus:ring-yellow-100 outline-none transition"
            placeholder="exemple@email.com"
          />

          <label htmlFor="password" className="font-semibold text-gray-700 flex items-center gap-2">
            <Lock className="w-4 h-4 text-yellow-500" />
            {t('forms.password') || "Mot de passe"}
          </label>
          <input
            id="password"
            name="password"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            minLength={6}
            autoComplete="current-password"
            aria-required="true"
            className="w-full px-4 py-2 rounded-lg border border-gray-200 focus:border-yellow-400 focus:ring-2 focus:ring-yellow-100 outline-none transition"
            placeholder="••••••"
          />

          <button
            type="submit"
            disabled={loading}
            className="mt-2 px-6 py-2 rounded-lg bg-yellow-400 hover:bg-yellow-500 text-gray-900 font-semibold shadow transition flex items-center justify-center gap-2"
          >
            {loading && <Loader2 className="animate-spin w-5 h-5" />}
            {t('navigation.login') || "Connexion"}
          </button>
        </form>
        {status && (
          <div
            className={`mt-6 px-4 py-3 rounded-lg text-sm font-medium flex items-center gap-2 ${
              status.type === 'error'
                ? 'bg-red-100 text-red-700'
                : 'bg-green-100 text-green-700'
            }`}
            role={status.type === 'error' ? 'alert' : 'status'}
            tabIndex={-1}
          >
            {status.message}
          </div>
        )}
        <div className="mt-8 text-xs text-gray-400 text-center">
          <span>
            <a href="/docs/contributing" className="underline hover:text-yellow-600">
              Contribuer au projet
            </a>
            {" • "}
            <a href="/docs/ajouter_metier" className="underline hover:text-yellow-600">
              Ajouter un métier
            </a>
          </span>
        </div>
      </section>
    </MainLayout>
  );
}

/**
 * Simulation d’authentification (à remplacer par l’intégration réelle).
 * @param {object} params
 * @returns {Promise<void>}
 */
async function fakeLogin(params) {
  await new Promise((r) => setTimeout(r, 300));
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('login_feature_consent');
}

/**
 * Valide une adresse email.
 * @param {string} email
 * @returns {boolean}
 */
function validateEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logLoginEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('login_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('login_logs', JSON.stringify(logs));
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
 * Efface les logs de login (droit à l’oubli RGPD).
 */
export function clearLocalLoginLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('login_logs');
  }
}
/**
 * @file Register.jsx
 * @description Page d’inscription pour Dihya Coding : design moderne, SEO, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

import React, { useState } from 'react';
import { useTranslation } from 'react-i18next';
import MainLayout from '../layout/MainLayout';
import { User, Mail, Lock, Loader2, ShieldCheck } from "lucide-react";

/**
 * Page d’inscription utilisateur.
 * @returns {JSX.Element}
 */
export default function Register() {
  const { t } = useTranslation();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirm, setConfirm] = useState('');
  const [status, setStatus] = useState(null);
  const [loading, setLoading] = useState(false);

  /**
   * Gère la soumission du formulaire d’inscription.
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
      setStatus({ type: 'error', message: t('forms.password_min_length') || 'Mot de passe trop court.' });
      return;
    }
    if (password !== confirm) {
      setStatus({ type: 'error', message: t('forms.passwords_mismatch') || 'Les mots de passe ne correspondent pas.' });
      return;
    }

    try {
      setLoading(true);
      await fakeRegister({ email, password });
      logRegisterEvent('register_success', {
        email: anonymizeEmail(email),
        timestamp: new Date().toISOString()
      });
      window.localStorage.setItem('current_user', JSON.stringify({ id: email, email, role: 'user', createdAt: new Date().toLocaleDateString() }));
      setStatus({ type: 'success', message: t('messages.register_success') || 'Inscription réussie.' });
      setEmail('');
      setPassword('');
      setConfirm('');
      // Redirection possible ici
    } catch (err) {
      logRegisterEvent('register_error', {
        email: anonymizeEmail(email),
        error: err.message,
        timestamp: new Date().toISOString()
      });
      setStatus({ type: 'error', message: t('messages.error_occurred') || "Erreur lors de l'inscription." });
    } finally {
      setLoading(false);
    }
  };

  return (
    <MainLayout title={t('navigation.register')} description={t('app.description')}>
      <section className="w-full max-w-md mx-auto bg-white/90 rounded-xl shadow-lg p-8 mt-12 mb-16 border border-gray-100 flex flex-col items-center" aria-labelledby="register-title">
        <div className="flex items-center gap-3 mb-4">
          <User className="w-8 h-8 text-yellow-500" />
          <h1 id="register-title" className="text-2xl font-bold text-gray-900 tracking-wide">
            {t('navigation.register') || "Inscription"}
          </h1>
        </div>
        <form onSubmit={handleSubmit} aria-describedby="register-desc" className="w-full flex flex-col gap-5">
          <div id="register-desc" className="sr-only">
            {t('app.description')}
          </div>
          <label htmlFor="email" className="font-semibold text-gray-700 flex items-center gap-2">
            <Mail className="w-4 h-4 text-yellow-500" />
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
            autoComplete="new-password"
            aria-required="true"
            className="w-full px-4 py-2 rounded-lg border border-gray-200 focus:border-yellow-400 focus:ring-2 focus:ring-yellow-100 outline-none transition"
            placeholder="••••••"
          />

          <label htmlFor="confirm" className="font-semibold text-gray-700 flex items-center gap-2">
            <Lock className="w-4 h-4 text-yellow-500" />
            {t('forms.confirm_password') || 'Confirmer le mot de passe'}
          </label>
          <input
            id="confirm"
            name="confirm"
            type="password"
            value={confirm}
            onChange={(e) => setConfirm(e.target.value)}
            required
            minLength={6}
            autoComplete="new-password"
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
            {t('navigation.register') || "Inscription"}
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
            <ShieldCheck className="w-5 h-5" />
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
 * Simulation d’inscription (à remplacer par l’intégration réelle).
 * @param {object} params
 * @returns {Promise<void>}
 */
async function fakeRegister(params) {
  await new Promise((r) => setTimeout(r, 350));
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('register_feature_consent');
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
function logRegisterEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('register_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('register_logs', JSON.stringify(logs));
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
 * Efface les logs d’inscription (droit à l’oubli RGPD).
 */
export function clearLocalRegisterLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('register_logs');
  }
}
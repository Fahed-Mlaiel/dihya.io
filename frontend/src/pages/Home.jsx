/**
 * @file Home.jsx
 * @description Page d’accueil de Dihya Coding : design moderne, SEO, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

import { BookOpen, GitBranch, Globe, Layers, Mic, ShieldCheck, Sparkles, Users } from "lucide-react";
import { useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import MainLayout from '../layout/MainLayout';

/**
 * Page d’accueil principale.
 * @returns {JSX.Element}
 */
export default function Home() {
  const { t, i18n } = useTranslation();

  useEffect(() => {
    if (hasConsent()) {
      logHomeEvent('home_view', { lang: i18n.language, path: window.location.pathname });
    }
  }, [i18n.language]);

  return (
    <MainLayout title={t('app.title')} description={t('app.description')}>
      <section className="w-full max-w-3xl mx-auto bg-white/90 rounded-xl shadow-lg p-10 mt-10 mb-16 border border-gray-100 flex flex-col items-center">
        <div className="flex items-center gap-3 mb-4">
          <Sparkles className="w-10 h-10 text-yellow-500" />
          <h1 id="home-title" className="text-4xl font-extrabold text-gray-900 tracking-wide">
            {t('app.title') || "Dihya Coding"}
          </h1>
        </div>
        <p className="text-lg text-gray-700 mb-6 text-center max-w-2xl">
          {t('app.description') || "La première plateforme No-Code / Low-Code souveraine pour générer tout projet numérique à partir d’un cahier des charges écrit ou vocal. Frontend, Backend, IA, DevOps, Blockchain, multilingue, sécurité, extensibilité, design moderne et héritage amazigh."}
        </p>
        <ul className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-8 w-full">
          <Feature icon={<Mic className="w-6 h-6 text-yellow-500" />} label="Entrée vocale & texte libre" />
          <Feature icon={<Layers className="w-6 h-6 text-yellow-500" />} label="Génération multi-stack (Web, Mobile, IA, DevOps, Blockchain…)" />
          <Feature icon={<ShieldCheck className="w-6 h-6 text-yellow-500" />} label="Sécurité, RGPD, auditabilité, souveraineté" />
          <Feature icon={<Globe className="w-6 h-6 text-yellow-500" />} label="Multilingue & dialectes inclus" />
          <Feature icon={<BookOpen className="w-6 h-6 text-yellow-500" />} label="Documentation claire & templates métiers prêts à l’emploi" />
          <Feature icon={<Users className="w-6 h-6 text-yellow-500" />} label="Marketplace de plugins & contribution ouverte" />
          <Feature icon={<GitBranch className="w-6 h-6 text-yellow-500" />} label="Déploiement automatique GitHub, CI/CD, preview live" />
        </ul>
        <a
          href="/generate"
          className="cta-btn px-8 py-3 rounded-lg bg-yellow-400 hover:bg-yellow-500 text-gray-900 font-bold text-lg shadow transition mb-4"
        >
          {t('generation.start') || "Générer un projet"}
        </a>
        <div className="text-xs text-gray-400 text-center mt-2">
          <span>
            <a href="https://github.com/DihyaCoding/templates" target="_blank" rel="noopener noreferrer" className="underline hover:text-yellow-600">
              Voir des exemples de templates métiers
            </a>
            {" • "}
            <a href="/docs/contributing" className="underline hover:text-yellow-600">
              Contribuer
            </a>
            {" • "}
            <a href="/docs/ajouter_metier" className="underline hover:text-yellow-600">
              Ajouter un métier
            </a>
          </span>
        </div>
        <footer className="mt-10 text-center text-xs text-gray-400">
          <span>
            Slogan : <i>De l’idée au code, en toute souveraineté.</i>
          </span>
        </footer>
      </section>
      <section className="w-full max-w-3xl mx-auto bg-white/90 rounded-xl shadow-lg p-6 mt-10 mb-10 border border-gray-100 flex flex-col items-center">
        <h2 className="text-2xl font-bold mb-2">Dashboard global conformité/monitoring</h2>
        <div style={{ display: 'flex', gap: 24, marginBottom: 16 }}>
          <img src="/Dihya/backend/compliance/reports/badge_conformite.svg" alt="Badge conformité backend" height={32} />
          <img src="/Dihya/backend/db/tests/coverage_db_badge.svg" alt="Badge couverture DB" height={32} />
        </div>
        <iframe
          title="Dashboard Global"
          src="/Dihya/backend/dashboard_global.md" // Peut être remplacé par .html si généré
          style={{ width: '100%', minHeight: 400, border: '1px solid #eee', borderRadius: 8, background: '#fff' }}
        />
        <a href="/dashboard-global" className="mt-2 text-blue-700 underline">Accéder au dashboard global interactif</a>
      </section>
    </MainLayout>
  );
}

/**
 * Composant Feature pour la liste des fonctionnalités clés.
 */
function Feature({ icon, label }) {
  return (
    <li className="flex items-center gap-3 bg-yellow-50 rounded-lg px-4 py-3 shadow-sm border border-yellow-100">
      {icon}
      <span className="text-gray-800 font-medium">{label}</span>
    </li>
  );
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('home_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logHomeEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('home_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('home_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs home (droit à l’oubli RGPD).
 */
export function clearLocalHomeLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('home_logs');
  }
}

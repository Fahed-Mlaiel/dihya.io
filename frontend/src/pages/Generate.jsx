/**
 * @file Generate.jsx
 * @description Générateur de projet Dihya Coding : design moderne, multilingue, sécurité, auditabilité, extensibilité, RGPD, UX avancée.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

import React, { useState } from 'react';
import { useTranslation } from 'react-i18next';
import MainLayout from '../layout/MainLayout';
import { Sparkles, ShieldCheck, Globe, Loader2 } from "lucide-react";

const MODULES = [
  { value: 'ai', label: 'IA' },
  { value: 'seo', label: 'SEO' },
  { value: 'ecommerce', label: 'E-commerce' },
  { value: 'security', label: 'Sécurité' },
  { value: 'blockchain', label: 'Blockchain' },
  { value: 'devops', label: 'DevOps' },
  { value: 'mobile', label: 'Mobile App' },
  { value: 'multilingue', label: 'Multilingue' }
];

export default function Generate() {
  const { t } = useTranslation();
  const [projectName, setProjectName] = useState('');
  const [modules, setModules] = useState([]);
  const [status, setStatus] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setStatus(null);

    if (!hasConsent()) {
      setStatus({ type: 'error', message: t('rgpd.consent_required') || "Consentement RGPD requis." });
      return;
    }
    if (!projectName.trim()) {
      setStatus({ type: 'error', message: t('forms.required') || "Nom du projet requis." });
      return;
    }
    if (modules.length === 0) {
      setStatus({ type: 'error', message: t('forms.required') || "Sélectionnez au moins un module." });
      return;
    }

    try {
      setLoading(true);
      await fakeGenerateProject({ projectName, modules });
      logGenerationEvent('generate_project', {
        projectName: anonymizeProjectName(projectName),
        modules,
        timestamp: new Date().toISOString()
      });
      setStatus({ type: 'success', message: t('generation.generation_success') || "Projet généré avec succès !" });
      setProjectName('');
      setModules([]);
    } catch (err) {
      setStatus({ type: 'error', message: t('messages.error_occurred') || "Une erreur est survenue." });
    } finally {
      setLoading(false);
    }
  };

  const handleModuleChange = (e) => {
    const { value, checked } = e.target;
    setModules((prev) =>
      checked ? [...prev, value] : prev.filter((m) => m !== value)
    );
  };

  return (
    <MainLayout title={t('generation.start')} description={t('app.description')}>
      <section className="w-full max-w-2xl mx-auto bg-white/90 rounded-xl shadow-lg p-8 mt-8 mb-16 border border-gray-100">
        <div className="flex items-center gap-3 mb-6">
          <Sparkles className="w-8 h-8 text-yellow-500" />
          <h1 className="text-3xl font-bold text-gray-900 tracking-wide" id="generate-title">
            {t('generation.start') || "Générer un projet"}
          </h1>
        </div>
        <form onSubmit={handleSubmit} aria-describedby="generate-desc" className="flex flex-col gap-6">
          <div id="generate-desc" className="sr-only">
            {t('app.description')}
          </div>
          <div>
            <label htmlFor="projectName" className="block text-gray-700 font-semibold mb-1">
              {t('generation.project_name') || "Nom du projet"}
            </label>
            <input
              id="projectName"
              name="projectName"
              type="text"
              value={projectName}
              onChange={(e) => setProjectName(e.target.value)}
              required
              minLength={3}
              maxLength={64}
              autoComplete="off"
              aria-required="true"
              className="w-full px-4 py-2 rounded-lg border border-gray-200 focus:border-yellow-400 focus:ring-2 focus:ring-yellow-100 outline-none transition"
              placeholder="Ex : Ma Startup, Plateforme RH, App IA..."
            />
          </div>
          <fieldset className="border border-gray-200 rounded-lg p-4">
            <legend className="font-semibold text-gray-700 mb-2">
              {t('generation.select_modules') || "Modules à inclure"}
            </legend>
            <div className="grid grid-cols-2 gap-3">
              {MODULES.map((mod) => (
                <label key={mod.value} className="flex items-center gap-2 text-gray-800">
                  <input
                    type="checkbox"
                    value={mod.value}
                    checked={modules.includes(mod.value)}
                    onChange={handleModuleChange}
                    aria-checked={modules.includes(mod.value)}
                    className="accent-yellow-500"
                  />
                  {mod.label}
                </label>
              ))}
            </div>
          </fieldset>
          <button
            type="submit"
            disabled={loading}
            className="mt-2 px-6 py-2 rounded-lg bg-yellow-400 hover:bg-yellow-500 text-gray-900 font-semibold shadow transition flex items-center justify-center gap-2"
          >
            {loading && <Loader2 className="animate-spin w-5 h-5" />}
            {t('generation.start') || "Générer"}
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
            {status.type === 'error' ? <ShieldCheck className="w-5 h-5" /> : <Globe className="w-5 h-5" />}
            {status.message}
          </div>
        )}
        <div className="mt-10 text-xs text-gray-400 text-center">
          <span>
            Toutes les générations sont <b>RGPD</b>, auditables, multilingues et extensibles.<br />
            <a href="https://github.com/DihyaCoding/templates" target="_blank" rel="noopener noreferrer" className="underline hover:text-yellow-600">
              Voir des exemples de templates métiers
            </a>
          </span>
        </div>
      </section>
    </MainLayout>
  );
}

// --- Fonctions utilitaires ---

async function fakeGenerateProject(params) {
  await new Promise((r) => setTimeout(r, 600));
}

function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('generation_feature_consent');
}

function logGenerationEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('generation_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('generation_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

function anonymizeProjectName(name) {
  if (!name) return '';
  return name.length > 4 ? name.slice(0, 2) + '***' + name.slice(-2) : '***';
}
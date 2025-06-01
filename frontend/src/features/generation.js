/**
 * @file generation.js
 * @description Fonctions de génération de projets, code et templates pour Dihya Coding.
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les interactions sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Lance la génération d’un projet via l’API backend.
 * @param {object} params - Paramètres de génération (nom, stack, options)
 * @param {string} params.name - Nom du projet
 * @param {string} params.stack - Stack technologique (ex: 'mern', 'django')
 * @param {object} [params.options] - Options avancées (thème, langue, modules)
 * @returns {Promise<object>} Résultat de la génération
 */
export async function generateProject({ name, stack, options = {} }) {
  validateProjectName(name);
  validateStack(stack);
  if (!window?.localStorage?.getItem('generation_feature_consent')) {
    throw new Error('Consentement requis pour utiliser la génération.');
  }
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/generate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { 'Authorization': `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ name, stack, options }),
  });
  if (!res.ok) throw new Error('Erreur lors de la génération du projet');
  const data = await res.json();
  logGenerationEvent('generate_project', anonymizeProjectName(name), stack);
  return data;
}

/**
 * Valide le nom du projet.
 * @param {string} name
 */
function validateProjectName(name) {
  if (!name || typeof name !== 'string' || name.length < 3 || name.length > 64) {
    throw new Error('Nom de projet invalide');
  }
}

/**
 * Valide la stack technologique.
 * @param {string} stack
 */
function validateStack(stack) {
  // Liste des stacks supportées (à synchroniser avec constants/stacks.js)
  const SUPPORTED_STACKS = [
    'mern', 'lamp', 'jamstack', 'python-flask', 'django', 'spring', 'dotnet', 'nextjs', 'vue', 'svelte'
  ];
  if (!SUPPORTED_STACKS.includes(stack)) {
    throw new Error('Stack technologique non supportée');
  }
}

/**
 * Anonymise le nom du projet pour les logs (pas de données personnelles).
 * @param {string} name
 * @returns {string}
 */
function anonymizeProjectName(name) {
  // Exemple simple : suppression d’emails
  return name.replace(/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/gi, '[email]');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} value
 * @param {string} [stack]
 */
function logGenerationEvent(action, value, stack) {
  try {
    const logs = JSON.parse(localStorage.getItem('generation_feature_logs') || '[]');
    logs.push({
      action,
      value,
      stack,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('generation_feature_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de génération locaux (droit à l’oubli RGPD).
 */
export function clearLocalGenerationLogs() {
  localStorage.removeItem('generation_feature_logs');
}
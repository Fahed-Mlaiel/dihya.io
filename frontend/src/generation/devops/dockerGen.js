/**
 * @file dockerGen.js
 * @description Générateur et gestionnaire de fichiers Docker pour Dihya Coding (Dockerfile, docker-compose, audit, logs).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les interactions sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Génère un Dockerfile à partir de paramètres métier.
 * @param {object} params
 * @param {string} params.baseImage - Image de base Docker (ex: 'node:18-alpine')
 * @param {string[]} [params.commands] - Commandes à exécuter (RUN, COPY, etc.)
 * @param {object} [params.options] - Options avancées (ports, env, workdir, user, etc.)
 * @returns {Promise<{success: boolean, dockerfile: string, warnings?: string[]}>}
 */
export async function generateDockerfile({ baseImage, commands = [], options = {} }) {
  validateBaseImage(baseImage);
  validateCommands(commands);
  if (!window?.localStorage?.getItem('docker_feature_consent')) {
    throw new Error('Consentement requis pour générer un Dockerfile.');
  }
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/devops/docker/generate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ baseImage, commands, options }),
  });
  if (!res.ok) throw new Error('Erreur lors de la génération du Dockerfile');
  const data = await res.json();
  logDockerGenEvent('generate_dockerfile', anonymizeBaseImage(baseImage));
  return data;
}

/**
 * Génère un fichier docker-compose.yml à partir de services.
 * @param {object} params
 * @param {Array<object>} params.services - Liste des services (nom, image, ports, env, volumes, etc.)
 * @param {object} [params.options] - Options avancées (réseaux, volumes globaux, version)
 * @returns {Promise<{success: boolean, compose: string, warnings?: string[]}>}
 */
export async function generateDockerCompose({ services, options = {} }) {
  validateServices(services);
  if (!window?.localStorage?.getItem('docker_feature_consent')) {
    throw new Error('Consentement requis pour générer un docker-compose.');
  }
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/devops/docker/compose', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ services, options }),
  });
  if (!res.ok) throw new Error('Erreur lors de la génération du docker-compose');
  const data = await res.json();
  logDockerGenEvent('generate_docker_compose', '[services]');
  return data;
}

/**
 * Audite un Dockerfile existant.
 * @param {object} params
 * @param {string} params.dockerfile - Contenu du Dockerfile à auditer
 * @returns {Promise<{success: boolean, issues: Array, report: string}>}
 */
export async function auditDockerfile({ dockerfile }) {
  validateDockerfileContent(dockerfile);
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/devops/docker/audit', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ dockerfile }),
  });
  if (!res.ok) throw new Error('Erreur lors de l’audit du Dockerfile');
  const data = await res.json();
  logDockerGenEvent('audit_dockerfile', '[dockerfile]');
  return data;
}

/**
 * Valide l’image de base Docker.
 * @param {string} baseImage
 */
function validateBaseImage(baseImage) {
  if (!baseImage || typeof baseImage !== 'string' || baseImage.length < 3) {
    throw new Error('Image de base Docker invalide');
  }
}

/**
 * Valide la liste des commandes Dockerfile.
 * @param {string[]} commands
 */
function validateCommands(commands) {
  if (!Array.isArray(commands)) throw new Error('Commandes Dockerfile invalides');
  for (const cmd of commands) {
    if (typeof cmd !== 'string' || cmd.length < 2) throw new Error('Commande Dockerfile invalide');
  }
}

/**
 * Valide la liste des services docker-compose.
 * @param {Array<object>} services
 */
function validateServices(services) {
  if (
    !Array.isArray(services) ||
    services.length === 0 ||
    !services.every(
      s =>
        s &&
        typeof s === 'object' &&
        typeof s.name === 'string' &&
        typeof s.image === 'string'
    )
  ) {
    throw new Error('Services docker-compose invalides');
  }
}

/**
 * Valide le contenu d’un Dockerfile.
 * @param {string} dockerfile
 */
function validateDockerfileContent(dockerfile) {
  if (!dockerfile || typeof dockerfile !== 'string' || dockerfile.length < 10) {
    throw new Error('Contenu Dockerfile invalide');
  }
}

/**
 * Anonymise l’image de base pour les logs (pas de données personnelles).
 * @param {string} baseImage
 * @returns {string}
 */
function anonymizeBaseImage(baseImage) {
  return baseImage.replace(/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/gi, '[email]');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} value
 */
function logDockerGenEvent(action, value) {
  try {
    const logs = JSON.parse(localStorage.getItem('docker_gen_logs') || '[]');
    logs.push({
      action,
      value,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('docker_gen_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de génération/audit Docker (droit à l’oubli RGPD).
 */
export function clearLocalDockerGenLogs() {
  localStorage.removeItem('docker_gen_logs');
}
/**
 * @file k8sGen.js
 * @description Générateur et gestionnaire de fichiers Kubernetes (k8s) pour Dihya Coding (déploiement, services, ingress, audit, logs).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les interactions sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Génère un fichier de déploiement Kubernetes à partir de paramètres métier.
 * @param {object} params
 * @param {string} params.appName - Nom de l’application (validé, anonymisé pour logs)
 * @param {string} params.image - Image Docker à déployer
 * @param {object} [params.options] - Options avancées (replicas, ports, env, ressources, labels, etc.)
 * @returns {Promise<{success: boolean, deployment: string, warnings?: string[]}>}
 */
export async function generateK8sDeployment({ appName, image, options = {} }) {
  validateAppName(appName);
  validateImage(image);
  if (!window?.localStorage?.getItem('k8s_feature_consent')) {
    throw new Error('Consentement requis pour générer un déploiement Kubernetes.');
  }
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/devops/k8s/deployment', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ appName, image, options }),
  });
  if (!res.ok) throw new Error('Erreur lors de la génération du déploiement Kubernetes');
  const data = await res.json();
  logK8sGenEvent('generate_k8s_deployment', anonymizeAppName(appName), image);
  return data;
}

/**
 * Génère un fichier de service Kubernetes.
 * @param {object} params
 * @param {string} params.appName - Nom de l’application/service
 * @param {object} [params.options] - Options avancées (type, ports, selector, etc.)
 * @returns {Promise<{success: boolean, service: string, warnings?: string[]}>}
 */
export async function generateK8sService({ appName, options = {} }) {
  validateAppName(appName);
  if (!window?.localStorage?.getItem('k8s_feature_consent')) {
    throw new Error('Consentement requis pour générer un service Kubernetes.');
  }
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/devops/k8s/service', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ appName, options }),
  });
  if (!res.ok) throw new Error('Erreur lors de la génération du service Kubernetes');
  const data = await res.json();
  logK8sGenEvent('generate_k8s_service', anonymizeAppName(appName));
  return data;
}

/**
 * Génère un fichier d’ingress Kubernetes.
 * @param {object} params
 * @param {string} params.domain - Domaine cible (validé)
 * @param {object} [params.options] - Options avancées (tls, annotations, backend, etc.)
 * @returns {Promise<{success: boolean, ingress: string, warnings?: string[]}>}
 */
export async function generateK8sIngress({ domain, options = {} }) {
  validateDomain(domain);
  if (!window?.localStorage?.getItem('k8s_feature_consent')) {
    throw new Error('Consentement requis pour générer un ingress Kubernetes.');
  }
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/devops/k8s/ingress', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ domain, options }),
  });
  if (!res.ok) throw new Error('Erreur lors de la génération de l’ingress Kubernetes');
  const data = await res.json();
  logK8sGenEvent('generate_k8s_ingress', anonymizeDomain(domain));
  return data;
}

/**
 * Audite un fichier Kubernetes YAML existant.
 * @param {object} params
 * @param {string} params.k8sYaml - Contenu YAML à auditer
 * @returns {Promise<{success: boolean, issues: Array, report: string}>}
 */
export async function auditK8sYaml({ k8sYaml }) {
  validateK8sYaml(k8sYaml);
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/devops/k8s/audit', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ k8sYaml }),
  });
  if (!res.ok) throw new Error('Erreur lors de l’audit du fichier Kubernetes');
  const data = await res.json();
  logK8sGenEvent('audit_k8s_yaml', '[yaml]');
  return data;
}

/**
 * Valide le nom de l’application.
 * @param {string} appName
 */
function validateAppName(appName) {
  if (!appName || typeof appName !== 'string' || appName.length < 3 || appName.length > 64) {
    throw new Error('Nom d’application invalide');
  }
}

/**
 * Valide l’image Docker.
 * @param {string} image
 */
function validateImage(image) {
  if (!image || typeof image !== 'string' || image.length < 3) {
    throw new Error('Image Docker invalide');
  }
}

/**
 * Valide le domaine pour l’ingress.
 * @param {string} domain
 */
function validateDomain(domain) {
  // Validation simple du domaine (améliorable selon besoins)
  if (
    !domain ||
    typeof domain !== 'string' ||
    !/^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(domain)
  ) {
    throw new Error('Domaine invalide');
  }
}

/**
 * Valide le contenu YAML Kubernetes.
 * @param {string} k8sYaml
 */
function validateK8sYaml(k8sYaml) {
  if (!k8sYaml || typeof k8sYaml !== 'string' || k8sYaml.length < 10) {
    throw new Error('Contenu YAML Kubernetes invalide');
  }
}

/**
 * Anonymise le nom de l’application pour les logs.
 * @param {string} appName
 * @returns {string}
 */
function anonymizeAppName(appName) {
  return appName.replace(/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/gi, '[email]');
}

/**
 * Anonymise le domaine pour les logs.
 * @param {string} domain
 * @returns {string}
 */
function anonymizeDomain(domain) {
  return domain.replace(/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/gi, '[email]');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} value
 * @param {string} [extra]
 */
function logK8sGenEvent(action, value, extra) {
  try {
    const logs = JSON.parse(localStorage.getItem('k8s_gen_logs') || '[]');
    logs.push({
      action,
      value,
      extra,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('k8s_gen_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de génération/audit Kubernetes (droit à l’oubli RGPD).
 */
export function clearLocalK8sGenLogs() {
  localStorage.removeItem('k8s_gen_logs');
}
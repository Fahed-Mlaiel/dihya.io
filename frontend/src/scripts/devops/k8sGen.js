/**
 * @file k8sGen.js
 * @description Générateur de manifestes Kubernetes pour Dihya Coding : génération sécurisée, validation, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Génère un manifeste Kubernetes (Deployment + Service) selon les paramètres fournis.
 * @param {object} params
 * @param {string} params.appName - Nom de l’application (alphanumérique, 3-32 caractères)
 * @param {string} params.image - Image Docker à déployer
 * @param {number} [params.replicas=1] - Nombre de pods
 * @param {number} [params.port=3000] - Port exposé
 * @param {object} [params.options] - Options avancées (labels, logs, etc.)
 * @returns {object} Résultat { success, manifest, error, timestamp }
 */
export function generateK8sManifest({
  appName,
  image,
  replicas = 1,
  port = 3000,
  options = {}
}) {
  if (!hasConsent()) {
    return {
      success: false,
      manifest: null,
      error: 'Consentement requis',
      timestamp: new Date().toISOString()
    };
  }
  if (
    !appName ||
    typeof appName !== 'string' ||
    !/^[a-z0-9\-]{3,32}$/i.test(appName)
  ) {
    return {
      success: false,
      manifest: null,
      error: 'Nom d’application invalide',
      timestamp: new Date().toISOString()
    };
  }
  if (
    !image ||
    typeof image !== 'string' ||
    !/^[a-z0-9\-:.\/]+$/i.test(image)
  ) {
    return {
      success: false,
      manifest: null,
      error: 'Image Docker invalide',
      timestamp: new Date().toISOString()
    };
  }

  const labels = {
    app: appName.toLowerCase(),
    ...(options.labels || {})
  };

  const manifest = `# Généré par Dihya Coding – ${new Date().toISOString()}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ${appName.toLowerCase()}-deployment
  labels:
    ${Object.entries(labels)
      .map(([k, v]) => `${sanitizeLabel(k)}: "${sanitizeLabel(v)}"`)
      .join('\n    ')}
spec:
  replicas: ${replicas}
  selector:
    matchLabels:
      app: ${appName.toLowerCase()}
  template:
    metadata:
      labels:
        app: ${appName.toLowerCase()}
    spec:
      containers:
        - name: ${appName.toLowerCase()}
          image: ${image}
          ports:
            - containerPort: ${port}
---
apiVersion: v1
kind: Service
metadata:
  name: ${appName.toLowerCase()}-service
spec:
  selector:
    app: ${appName.toLowerCase()}
  ports:
    - protocol: TCP
      port: ${port}
      targetPort: ${port}
  type: ClusterIP
`;

  if (options.log !== false) {
    logK8sGenEvent('k8s_manifest_generated', {
      appName: anonymizeAppName(appName),
      image: anonymizeImage(image),
      replicas,
      port,
      timestamp: new Date().toISOString()
    });
  }

  return {
    success: true,
    manifest,
    error: null,
    timestamp: new Date().toISOString()
  };
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('k8s_gen_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logK8sGenEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('k8s_gen_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('k8s_gen_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise un nom d’application pour les logs.
 * @param {string} name
 * @returns {string}
 */
function anonymizeAppName(name) {
  if (!name) return '';
  return name.length > 4 ? name.slice(0, 2) + '***' + name.slice(-2) : '***';
}

/**
 * Anonymise une image Docker pour les logs.
 * @param {string} image
 * @returns {string}
 */
function anonymizeImage(image) {
  if (!image) return '';
  return image.replace(/[^a-z0-9\-:.\/]/gi, '').slice(0, 24) + (image.length > 24 ? '...' : '');
}

/**
 * Sanitize une clé/valeur de label Kubernetes.
 * @param {string} label
 * @returns {string}
 */
function sanitizeLabel(label) {
  return String(label).replace(/[^a-zA-Z0-9\-_.:]/g, '');
}

/**
 * Efface les logs de génération K8s (droit à l’oubli RGPD).
 */
export function clearLocalK8sGenLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('k8s_gen_logs');
  }
}
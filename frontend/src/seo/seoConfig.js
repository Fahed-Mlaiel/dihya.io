/**
 * @file seoConfig.js
 * @description Configuration SEO centrale pour Dihya Coding : balises meta, titres, descriptions, canonical, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Retourne la configuration SEO par défaut pour l’application.
 * @param {object} [overrides] - Surcharges personnalisées (title, description, canonical, robots, etc.)
 * @returns {object} Objet de configuration SEO
 */
export function getDefaultSeoConfig(overrides = {}) {
  const config = {
    title: 'Dihya Coding – Génération de code moderne, sécurisée et conforme RGPD',
    description: 'Plateforme de génération de code, d’outils et de pages web modernes, robustes, accessibles, sécurisées et conformes RGPD.',
    canonical: 'https://dihya.app/',
    robots: 'index, follow',
    og: {
      type: 'website',
      title: 'Dihya Coding',
      description: 'Générez du code moderne, sécurisé et conforme RGPD pour chaque génération.',
      url: 'https://dihya.app/',
      image: 'https://dihya.app/assets/og-image.png'
    },
    twitter: {
      card: 'summary_large_image',
      site: '@dihya_coding',
      title: 'Dihya Coding',
      description: 'Générez du code moderne, sécurisé et conforme RGPD pour chaque génération.',
      image: 'https://dihya.app/assets/og-image.png'
    },
    ...sanitizeSeoOverrides(overrides)
  };

  if (hasConsent()) {
    logSeoConfigEvent('seo_config_generated', {
      title: anonymizeTitle(config.title),
      canonical: anonymizeCanonical(config.canonical),
      timestamp: new Date().toISOString()
    });
  }

  return config;
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('seo_config_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logSeoConfigEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('seo_config_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('seo_config_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Sanitize les surcharges SEO pour éviter l’injection.
 * @param {object} overrides
 * @returns {object}
 */
function sanitizeSeoOverrides(overrides) {
  const sanitized = {};
  Object.entries(overrides || {}).forEach(([k, v]) => {
    if (typeof v === 'string') {
      sanitized[k] = v.replace(/[\r\n<>]/g, '');
    } else if (typeof v === 'object' && v !== null) {
      sanitized[k] = sanitizeSeoOverrides(v);
    } else {
      sanitized[k] = v;
    }
  });
  return sanitized;
}

/**
 * Anonymise un titre pour les logs.
 * @param {string} title
 * @returns {string}
 */
function anonymizeTitle(title) {
  if (!title) return '';
  return title.length > 16 ? title.slice(0, 8) + '...' : title;
}

/**
 * Anonymise une URL canonical pour les logs.
 * @param {string} url
 * @returns {string}
 */
function anonymizeCanonical(url) {
  if (!url) return '';
  return url.replace(/\/\/[^/]+\//, '//***/');
}

/**
 * Efface les logs SEO config (droit à l’oubli RGPD).
 */
export function clearLocalSeoConfigLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('seo_config_logs');
  }
}
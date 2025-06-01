/**
 * @file performance.js
 * @description Module de monitoring des performances pour Dihya Coding (web vitals, UX, SEO, RGPD, auditabilité).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les mesures sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

const VITALS = ['FCP', 'LCP', 'CLS', 'FID', 'TTFB'];

/**
 * Initialise le monitoring des performances (web vitals).
 * @param {object} [options]
 * @param {boolean} [options.log=true] - Active le log local pour auditabilité
 * @param {function} [options.onReport] - Callback personnalisé pour chaque mesure
 */
export function initPerformanceMonitoring(options = {}) {
  if (!hasConsent()) return;
  if (typeof window === 'undefined' || !window.performance) return;

  // Utilisation de PerformanceObserver pour les web vitals
  try {
    if ('PerformanceObserver' in window) {
      const observer = new window.PerformanceObserver((list) => {
        for (const entry of list.getEntries()) {
          const metric = mapPerformanceEntry(entry);
          if (metric && VITALS.includes(metric.name)) {
            if (options.log !== false) {
              logPerformanceEvent('web_vital', metric);
            }
            if (typeof options.onReport === 'function') {
              options.onReport(metric);
            }
          }
        }
      });
      observer.observe({ type: 'paint', buffered: true });
      observer.observe({ type: 'largest-contentful-paint', buffered: true });
      observer.observe({ type: 'layout-shift', buffered: true });
      observer.observe({ type: 'first-input', buffered: true });
      observer.observe({ type: 'navigation', buffered: true });
    }
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Mappe une entrée PerformanceEntry en métrique standardisée.
 * @param {PerformanceEntry} entry
 * @returns {object|null}
 */
function mapPerformanceEntry(entry) {
  switch (entry.entryType) {
    case 'paint':
      if (entry.name === 'first-contentful-paint') {
        return { name: 'FCP', value: entry.startTime, timestamp: Date.now() };
      }
      break;
    case 'largest-contentful-paint':
      return { name: 'LCP', value: entry.startTime, timestamp: Date.now() };
    case 'layout-shift':
      if (!entry.hadRecentInput && entry.value > 0) {
        return { name: 'CLS', value: entry.value, timestamp: Date.now() };
      }
      break;
    case 'first-input':
      return { name: 'FID', value: entry.processingStart - entry.startTime, timestamp: Date.now() };
    case 'navigation':
      return { name: 'TTFB', value: entry.responseStart, timestamp: Date.now() };
    default:
      return null;
  }
  return null;
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('performance_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logPerformanceEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('performance_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('performance_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de performance (droit à l’oubli RGPD).
 */
export function clearLocalPerformanceLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('performance_logs');
  }
}
/**
 * @file test_scripts.js
 * @description Scripts de tests pour Dihya Coding : tests unitaires, intégration, robustesse, sécurité, conformité RGPD, auditabilité, extensibilité et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Lance un test unitaire sécurisé.
 * @param {string} name - Nom du test
 * @param {function} fn - Fonction de test à exécuter
 * @param {object} [options]
 * @param {boolean} [options.log=true] - Active le log local pour auditabilité
 * @returns {object} Résultat { name, success, error, timestamp }
 */
export function runUnitTest(name, fn, options = {}) {
  if (!hasConsent()) {
    return {
      name,
      success: false,
      error: 'Consentement requis',
      timestamp: new Date().toISOString()
    };
  }
  let success = false;
  let error = null;
  try {
    fn();
    success = true;
  } catch (err) {
    error = err.message;
  }
  if (options.log !== false) {
    logTestEvent('unit_test', {
      name: anonymizeTestName(name),
      success,
      error,
      timestamp: new Date().toISOString()
    });
  }
  return { name, success, error, timestamp: new Date().toISOString() };
}

/**
 * Lance une suite de tests et retourne un rapport global.
 * @param {Array<{name: string, fn: function}>} tests
 * @param {object} [options]
 * @returns {object} Rapport { total, passed, failed, results, timestamp }
 */
export function runTestSuite(tests, options = {}) {
  if (!Array.isArray(tests)) throw new Error('Liste de tests invalide');
  const results = tests.map(test =>
    runUnitTest(test.name, test.fn, options)
  );
  const passed = results.filter(r => r.success).length;
  const failed = results.length - passed;
  if (options.log !== false && hasConsent()) {
    logTestEvent('test_suite', {
      total: results.length,
      passed,
      failed,
      timestamp: new Date().toISOString()
    });
  }
  return {
    total: results.length,
    passed,
    failed,
    results,
    timestamp: new Date().toISOString()
  };
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('test_scripts_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logTestEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('test_scripts_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('test_scripts_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise un nom de test pour les logs.
 * @param {string} name
 * @returns {string}
 */
function anonymizeTestName(name) {
  if (!name) return '';
  return name.length > 8 ? name.slice(0, 4) + '***' + name.slice(-2) : '***';
}

/**
 * Efface les logs de tests (droit à l’oubli RGPD).
 */
export function clearLocalTestScriptsLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('test_scripts_logs');
  }
}
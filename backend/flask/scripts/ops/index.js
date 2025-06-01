// index.js - Script avancé d’opérations (ops, audit, RGPD, plugins, multitenancy)
// Compatible Linux, Codespaces, CI, Docker

// Imports métiers, plugins, audit, RGPD, monitoring, sécurité
const { logAudit, logSecurity, logOps } = require('../../../utils/audit');
const { anonymize, exportData, checkConsent } = require('../../../utils/rgpd');
const { loadPlugin, runPluginHook } = require('../../../plugins');
const { getTenantContext } = require('../../../utils/multitenant');
const { checkStatus, sendAlert } = require('../../../utils/monitoring');
const { checkRole, antiAbuse } = require('../../../utils/security');

/**
 * Exécute une opération métier avancée (audit, RGPD, plugins, multitenancy, monitoring, sécurité, CI/CD)
 * @param {string} operation - Nom de l'opération ("audit", "rgpd", "plugin", "tenant", "monitoring", "security", "reporting")
 * @param {object} context - Contexte d'exécution (user, tenant, data, plugin, etc.)
 * @returns {object} Résultat détaillé de l'opération
 */
function runOps(operation, context = {}) {
  const { user, tenant, data, plugin, route, action } = context;
  let result = { success: false, details: {}, operation, timestamp: new Date().toISOString() };
  try {
    // Sécurité & anti-abus
    if (user && !checkRole(user, operation)) throw new Error('Accès refusé');
    antiAbuse(user, route, action);
    // Multitenancy
    const tenantCtx = tenant ? getTenantContext(tenant) : null;
    // Audit
    logAudit(operation, user, { tenant, route, action });
    // RGPD
    if (operation === 'rgpd') {
      checkConsent(user);
      result.details.anonymized = anonymize(data);
      result.details.export = exportData(user, data);
    }
    // Plugins métiers
    if (operation === 'plugin' && plugin) {
      const loaded = loadPlugin(plugin);
      result.details.pluginResult = runPluginHook(loaded, action, data);
    }
    // Monitoring
    if (operation === 'monitoring') {
      result.details.status = checkStatus();
      if (result.details.status.alert) sendAlert(result.details.status);
    }
    // Sécurité
    if (operation === 'security') {
      logSecurity(user, action, route);
    }
    // Reporting CI/CD
    if (operation === 'reporting') {
      logOps('reporting', { user, tenant, route, action });
      // Générer un rapport structuré pour la CI/CD
      result.details.report = {
        status: 'ok',
        timestamp: result.timestamp,
        user,
        tenant,
        route,
        action
      };
    }
    result.success = true;
  } catch (e) {
    result.error = e.message;
    logAudit('ops_error', user, { error: e.message, operation, tenant, route, action });
  }
  return result;
}

module.exports = { runOps };

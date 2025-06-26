// index.js ultra avancé pour les tests centralisés Plugins (Node.js)
// Point d'entrée pour tous les tests de plugins métiers, audit, générateurs, etc.

const testAuditPlugin = require('./audit/test_audit_plugin');
const testPlugin = require('./generators/test_plugin');
const testPluginJs = require('./generators/test_plugin_js');
const auditPlugin = require('../../plugins/audit/audit_plugin.js');
// Ajoutez ici d'autres tests plugins à exposer

describe('auditPlugin', () => {
  it('existe', () => {
    expect(typeof auditPlugin).toBe('function');
  });
});

module.exports = {
  testAuditPlugin,
  testPlugin,
  testPluginJs,
  // Ajoutez d'autres exports ici selon l'évolution des tests
};

/**
 * Exemple d'utilisation :
 * const { testAuditPlugin } = require('./plugins');
 * testAuditPlugin();
 */

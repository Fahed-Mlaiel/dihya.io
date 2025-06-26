// Test centralisé ultra avancé pour le générateur de plugin JS
const { createPlugin } = require('../../../plugins/generators/plugin');

test('createPlugin génère un plugin clé en main', () => {
    const plugin = createPlugin('Inventaire', { version: 1 }, { onStart: () => true });
    expect(plugin.metier).toBe('Inventaire');
    expect(plugin.enabled).toBe(true);
    expect(plugin.config.version).toBe(1);
    expect(typeof plugin.activate).toBe('function');
    expect(plugin.activate()).toBe('Plugin Inventaire activé');
    expect(plugin.deactivate()).toBe('Plugin Inventaire désactivé');
});

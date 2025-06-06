/* global console */
// pluginManager.sample.js
// Exemple d'utilisation du pluginManager (JS)
const pluginManager = require('../core/pluginManager');

// Exemple : enregistrement et exécution d'un plugin
pluginManager.register('test', () => 'ok');
console.log('Résultat plugin test:', pluginManager.run('test'));

// sample_plugin.js
// Exemple de plugin (sample) pour le module core plugins threed.
// Sert de référence pour l'intégration, la documentation et les tests.

class SamplePlugin {
  constructor(options = {}) {
    this.options = options;
  }

  /**
   * Initialise le sample plugin avec des paramètres de test.
   * @param {Object} config - Configuration de test.
   */
  init(config) {
    this.config = config;
    // Logique d'initialisation de sample
    return true;
  }

  /**
   * Exécute la fonctionnalité principale du sample plugin.
   * @param {any} data - Données à traiter.
   * @returns {any} Résultat du traitement sample.
   */
  run(data) {
    // Traitement métier de sample
    return { processed: true, data, config: this.config };
  }
}

module.exports = SamplePlugin;

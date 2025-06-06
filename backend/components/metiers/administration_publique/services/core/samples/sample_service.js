// sample_service.js
// Exemple de service (sample) pour le module core services threed.
// Sert de référence pour l'intégration, la documentation et les tests.

class SampleService {
  constructor(options = {}) {
    this.options = options;
    this.state = 'ready';
  }

  /**
   * Initialise le sample service avec des paramètres de test.
   * @param {Object} config - Configuration de test.
   */
  init(config) {
    this.config = config;
    this.state = 'initialized';
    return true;
  }

  /**
   * Exécute la fonctionnalité principale du sample service.
   * @param {any} data - Données à traiter.
   * @returns {any} Résultat du traitement sample.
   */
  run(data) {
    return { processed: true, data, config: this.config, state: this.state };
  }
}

module.exports = SampleService;

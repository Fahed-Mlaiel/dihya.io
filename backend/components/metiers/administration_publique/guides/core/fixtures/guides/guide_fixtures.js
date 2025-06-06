// guide_fixtures.js - Guide d'utilisation avancée des fixtures Threed (JS)

/**
 * Ce fichier documente les bonnes pratiques pour la création, la gestion et l'utilisation des fixtures JS dans Threed.
 *
 * Exemples :
 *   - Génération dynamique de fixtures
 *   - Synchronisation avec les tests Python
 *   - Utilisation dans la CI/CD
 */

module.exports = {
  doc: 'Voir README_ADVANCED.md pour les exemples détaillés.'
};

/**
 * Exemples avancés :
 *
 * // Génération dynamique
 * const { generateModel } = require('../fixtures/fixtures.generator');
 * const model = generateModel('StressTest', 100, 200);
 *
 * // Synchronisation avec Python :
 * // Voir fixtures.py et fixtures_generator.py
 *
 * // Utilisation en CI/CD :
 * // npm run test:fixtures
 *
 * // Edge cases : modèles vides, assets manquants, etc.
 */

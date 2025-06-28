// Exemple d’intégration API Node.js ultra avancé
import { apiHello } from '../../../../nodejs/api/api_helper.js';

/**
 * Exécute un scénario d’intégration API métier Node.js
 */
export function runApiSample() {
  console.log('--- API Node.js Sample ---');
  console.log(apiHello());
}

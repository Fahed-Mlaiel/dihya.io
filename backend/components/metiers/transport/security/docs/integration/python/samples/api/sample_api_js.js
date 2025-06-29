/* global console */
// Exemple ultra avancé d’intégration API JS côté Python
import { apiHello } from '../../api/api_helper.js';

export function runApiSample() {
  console.log('--- API Python Sample (JS) ---');
  console.log(apiHello());
}

if (require.main === module) {
  runApiSample();
}

// Exemple ultra avancé d’intégration API Node.js
import { apiHello } from '../../api/api_helper.js';

export function runApiSample() {
  console.log('--- API Node.js Sample ---');
  console.log(apiHello());
}

// Pour exécution directe
if (require.main === module) {
  runApiSample();
}

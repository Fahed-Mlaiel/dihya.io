// Exemple avancé d’intégration RBAC JS côté Python
import { rbacHello } from '../../rbac/rbac_helper.js';

export function runRbacSample() {
  console.log('--- RBAC Python Sample (JS) ---');
  console.log(rbacHello());
}

if (require.main === module) {
  runRbacSample();
}

// Exemple avancé d’intégration RBAC Node.js
import { rbacHello } from '../../rbac/rbac_helper.js';

export function runRbacSample() {
  console.log('--- RBAC Node.js Sample ---');
  console.log(rbacHello());
}

if (require.main === module) {
  runRbacSample();
}

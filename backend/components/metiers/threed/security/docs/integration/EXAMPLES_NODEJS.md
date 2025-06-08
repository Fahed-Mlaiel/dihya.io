# Exemples d’intégration Sécurité 3D (Node.js)

```js
const { policy, crypto, accessControl } = require('../core');
const { logs, reports } = require('../audit/samples');

// Exemple : Vérification d’accès
if (accessControl.checkAccess(user, 'admin')) {
  // ...
}

// Exemple : Génération de rapport d’audit
const report = reports.sample_audit_report.generateAuditReport(...);
```

---

# 3D Security Integration Examples (EN)

See code samples above for Node.js integration with core and audit modules.

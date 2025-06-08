# Exemples d’intégration Sécurité 3D (Python)

```python
from core import policy, crypto, access_control
from audit.samples import logs, reports

# Exemple : Vérification d’accès
if access_control.check_access(user, 'admin'):
    ...

# Exemple : Génération de rapport d’audit
report = reports.sample_audit_report.generate_audit_report(...)
```

---

# 3D Security Integration Examples (EN)

See code samples above for Python integration with core and audit modules.

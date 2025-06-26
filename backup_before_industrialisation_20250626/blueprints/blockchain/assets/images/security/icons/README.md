# Security Icons

Ce dossier regroupe toutes les icônes SVG liées à la sécurité : audit, scan, conformité, firewall, WAF, etc.

## Fichiers inclus
- `audit_log.svg` : Icône d’audit log
- `security_scan.svg` : Icône de scan de sécurité
- `compliance_check.svg` : Icône de vérification de conformité
- `firewall.svg` : Icône de firewall
- `waf.svg` : Icône de Web Application Firewall

## Bonnes pratiques Lead Dev
- Utiliser ces icônes dans les dashboards, alertes, pages de sécurité, documentation, etc.
- Préférer SVG pour la qualité et la personnalisation
- Centraliser les imports via `index.js`

## Exemple d’intégration (React)
```jsx
import { AuditLog, SecurityScan } from './index.js';

function SecurityIcons() {
  return <>
    <img src={AuditLog} alt="Audit Log" />
    <img src={SecurityScan} alt="Security Scan" />
  </>;
}
```

## Contact
Pour toute nouvelle icône, respecter la charte graphique et valider avec le Lead Dev.

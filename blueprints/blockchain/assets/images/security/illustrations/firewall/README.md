# Firewall Illustrations

Ce dossier regroupe toutes les illustrations SVG liées à la protection réseau : firewall, WAF, rate limiting, anti-DDoS, etc.

## Fichiers inclus
- `firewall.svg` : Illustration du firewall
- `waf.svg` : Illustration du Web Application Firewall
- `rate_limiting.svg` : Illustration de la limitation de débit
- `anti_ddos.svg` : Illustration de la protection anti-DDoS

## Bonnes pratiques Lead Dev
- Utiliser ces illustrations dans la documentation, les guides utilisateurs, les interfaces de sécurité, etc.
- Préférer SVG pour la qualité et la personnalisation
- Centraliser les imports via `index.js`

## Exemple d’intégration (React)
```jsx
import { Firewall, Waf } from './index.js';

function FirewallAssets() {
  return <>
    <img src={Firewall} alt="Firewall" />
    <img src={Waf} alt="WAF" />
  </>;
}
```

## Contact
Pour toute nouvelle illustration, respecter la charte graphique et valider avec le Lead Dev.

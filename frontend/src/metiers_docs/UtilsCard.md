# UtilsCard

## Description
Carte utilitaire pour la gestion avancée des modules IA, VR, AR, etc. Fournit des fonctions réutilisables, multilingues, sécurisées et extensibles.

## Fonctions principales
- Conversion de formats (JSON, XML, CSV)
- Génération d'identifiants uniques (UUIDv4)
- Gestion des erreurs multilingues
- Sécurité (hash, validation, filtrage XSS)
- Support multitenancy

## Exemple d'utilisation
```js
import { generateUUID, formatError } from '../utils/UtilsCard';

const id = generateUUID();
const err = formatError('Accès refusé', 'fr');
```

## Internationalisation
Supporte : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.

## Sécurité
Toutes les fonctions sont testées contre les injections, XSS, et respectent la RGPD.

## Extensibilité
Ajoutez vos propres utilitaires via le système de plugins (voir ./plugins/README.md).

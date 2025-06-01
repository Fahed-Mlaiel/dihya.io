# VrArCard

## Description
Carte métier pour la gestion de la Réalité Virtuelle (VR) et Augmentée (AR) dans les projets IA, web, mobile, etc.

## Fonctions principales
- Initialisation de scènes 3D/AR
- Intégration IA (agents, objets intelligents)
- Sécurité (sandbox, permissions)
- Multitenancy (espaces partagés)

## Exemple d'utilisation
```js
import { initVRScene, addAIObject } from '../vrar/VrArCard';

const scene = initVRScene('fr');
addAIObject(scene, { type: 'assistant', lang: 'fr' });
```

## Internationalisation
Supporte : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.

## Sécurité
Sandbox, logs, auditabilité, RGPD.

## Extensibilité
Ajoutez vos propres modules VR/AR via plugins.

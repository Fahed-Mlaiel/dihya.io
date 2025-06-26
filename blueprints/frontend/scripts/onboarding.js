// onboarding.js
// Script d’onboarding automatisé (Lead Dev)
// Génère un guide d’onboarding personnalisé pour les nouveaux devs frontend

const fs = require('fs');
const path = require('path');

const guide = `# Onboarding Frontend – Dihya.io

Bienvenue !

## 1. Installation
- Cloner le repo
- Installer Node.js, npm, Docker
- Lancer : npm ci && npm run build

## 2. Structure du projet
- Voir le dossier src/ (atomic design, features, hooks, services, plugins, assets, i18n, devops, etc.)

## 3. Scripts utiles
- Génération complète : node scripts/generate_full_frontend.js
- Migration : node scripts/migrate_frontend.js
- Audit : node devops/audit_components.js

## 4. Bonnes pratiques
- Respecter les conventions, la doc, la checklist Lead Dev
- Pas de placeholder, pas de doublon, pas de fichier vide

Bon courage !
`;

fs.writeFileSync(path.join(__dirname, 'ONBOARDING.md'), guide);
console.log('✅ Guide d’onboarding généré : ONBOARDING.md');

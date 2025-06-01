#!/usr/bin/env node
// Test d'intégration Node.js ultra avancé pour favicons API backend Dihya
const { execSync } = require('child_process');

try {
  execSync('python3 audit_favicons.py', { stdio: 'inherit' });
  execSync('node audit_favicons.js', { stdio: 'inherit' });
  execSync('python3 test_favicons.py', { stdio: 'inherit' });
  execSync('bash svg2png_favicons.sh', { stdio: 'inherit' });
  console.log('Intégration CI/CD favicons API backend Dihya : OK');
} catch (e) {
  console.error('Erreur CI/CD favicons API backend Dihya', e);
  process.exit(1);
}

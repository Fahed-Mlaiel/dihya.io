#!/usr/bin/env node
// Test d'intégration Node.js ultra avancé pour illustrations backend Dihya
const { execSync } = require('child_process');

try {
  execSync('python3 audit_illustrations.py', { stdio: 'inherit' });
  execSync('node audit_illustrations.js', { stdio: 'inherit' });
  console.log('Intégration CI/CD illustrations backend Dihya : OK');
} catch (e) {
  console.error('Erreur CI/CD illustrations backend Dihya', e);
  process.exit(1);
}

#!/usr/bin/env node
// sync_metiers_with_environnement.js – Synchronise tous les dossiers métiers avec le modèle "environnement"
// Usage: node sync_metiers_with_environnement.js

const fs = require('fs');
const path = require('path');

const METIERS_ROOT = path.resolve(__dirname, 'backend/components/metiers');
const ENV_MODEL = path.join(METIERS_ROOT, 'environnement');

function listMetiers() {
  return fs.readdirSync(METIERS_ROOT).filter(
    d => fs.statSync(path.join(METIERS_ROOT, d)).isDirectory() && d !== 'environnement' && !d.startsWith('.')
  );
}

function syncDir(src, dest, log = []) {
  if (!fs.existsSync(dest)) fs.mkdirSync(dest);
  for (const file of fs.readdirSync(src)) {
    const srcPath = path.join(src, file);
    const destPath = path.join(dest, file);
    const stat = fs.statSync(srcPath);
    if (stat.isDirectory()) {
      syncDir(srcPath, destPath, log);
    } else {
      if (!fs.existsSync(destPath) || fs.readFileSync(srcPath, 'utf8') !== fs.readFileSync(destPath, 'utf8')) {
        fs.copyFileSync(srcPath, destPath);
        log.push(`MAJ: ${destPath}`);
      }
    }
  }
}

function main() {
  const metiers = listMetiers();
  const report = [];
  for (const metier of metiers) {
    const metierPath = path.join(METIERS_ROOT, metier);
    report.push(`\n=== Synchronisation: ${metier} ===`);
    syncDir(ENV_MODEL, metierPath, report);
  }
  fs.writeFileSync(path.join(METIERS_ROOT, 'sync_report.txt'), report.join('\n'));
  console.log('Synchronisation terminée. Rapport: backend/components/metiers/sync_report.txt');
}

main();

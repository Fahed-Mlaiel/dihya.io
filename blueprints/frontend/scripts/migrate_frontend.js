// migrate_frontend.js
// Script de migration avancée (Lead Dev)
// Permet de migrer la structure, les assets, les hooks, les services, etc. d’une version à l’autre

const fs = require('fs');
const path = require('path');

function migrateFile(src, dest) {
  if (fs.existsSync(src)) {
    fs.copyFileSync(src, dest);
    console.log(`✅ Migré : ${src} -> ${dest}`);
  }
}

// Exemple d’utilisation : node migrate_frontend.js src/hooks src/hooks_v2
const [,, from, to] = process.argv;
if (!from || !to) {
  console.error('Usage : node migrate_frontend.js <from> <to>');
  process.exit(1);
}

if (!fs.existsSync(to)) fs.mkdirSync(to, { recursive: true });
fs.readdirSync(from).forEach(f => migrateFile(path.join(from, f), path.join(to, f)));

console.log('✅ Migration terminée');

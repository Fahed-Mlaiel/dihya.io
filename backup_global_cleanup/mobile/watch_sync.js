// Watcher automatique pour synchronisation frontend -> mobile
// Usage : node watch_sync.js

const chokidar = require('chokidar');
const { exec } = require('child_process');
const path = require('path');

const SRC = path.resolve(__dirname, '../frontend/src');
const SYNC_SCRIPT = path.resolve(__dirname, './sync_frontend_to_mobile.js');

console.log('⏳ Surveillance des changements dans frontend/src...');

chokidar.watch(SRC, { ignoreInitial: true }).on('all', (event, pathChanged) => {
  console.log(`🔄 Changement détecté (${event}) sur : ${pathChanged}`);
  exec(`node ${SYNC_SCRIPT}`, (err, stdout, stderr) => {
    if (err) {
      console.error('Erreur de synchronisation :', stderr);
    } else {
      console.log('✅ Synchronisation mobile terminée.');
    }
  });
});

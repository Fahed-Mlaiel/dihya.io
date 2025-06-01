// push_dashboard_ws.js
// Script Node.js pour push automatique du dashboard global ou d’alertes/logs via WebSocket (CI/CD, monitoring, alerting)

const fs = require('fs');
const path = require('path');
const WebSocket = require('ws');

const DASHBOARD_MD_PATH = path.join(__dirname, '../../dashboard_global.md');
const WS_URL = process.env.DASHBOARD_WS_URL || 'ws://localhost:8081/ws/dashboard';

function pushDashboard() {
  const md = fs.readFileSync(DASHBOARD_MD_PATH, 'utf-8');
  const ws = new WebSocket(WS_URL);
  ws.on('open', () => {
    ws.send(md);
    setTimeout(() => ws.close(), 1000);
  });
}

function pushAlert(message) {
  const ws = new WebSocket(WS_URL);
  ws.on('open', () => {
    ws.send('alert:' + message);
    setTimeout(() => ws.close(), 1000);
  });
}

if (require.main === module) {
  const arg = process.argv[2];
  if (arg === 'alert') {
    pushAlert(process.argv.slice(3).join(' ') || 'Alerte personnalisée !');
  } else {
    pushDashboard();
  }
}

module.exports = { pushDashboard, pushAlert };

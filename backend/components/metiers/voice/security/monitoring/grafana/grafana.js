/* global console */
// grafana.js – Setup dashboard sécurité

function grafanaLog(msg) {
  console.log(msg);
}

function setupGrafanaDashboard() {
  grafanaLog('Dashboard sécurité Grafana prêt.');
}

module.exports = { setupGrafanaDashboard };

/* global console */
// prometheus.js – Export des métriques sécurité

function prometheusLog(msg) {
  console.log(msg);
}

function exportMetrics() {
  prometheusLog('# HELP security_access_denied_total Nombre d\'accès refusés');
  prometheusLog('security_access_denied_total 0');
}

module.exports = { exportMetrics };

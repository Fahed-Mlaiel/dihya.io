/* global console */
// prometheus.js – Export des métriques sécurité

function exportMetrics() {
  console.log('# HELP security_access_denied_total Nombre d\'accès refusés');
  console.log('security_access_denied_total 0');
}

module.exports = { exportMetrics };

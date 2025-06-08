// sample_monitoring.js
// Exemple d’intégration avancée pour la supervision

const { sendAlert, generateDashboard } = require('./helpers_monitoring');

sendAlert('CPU usage high');
console.log(generateDashboard({ cpu: 90, ram: 80 }));

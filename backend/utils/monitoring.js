// Mock monitoring (statut, alertes)
function checkStatus() { return { status: 'ok', alert: false }; }
function sendAlert(status) { return { alert: true, status }; }
module.exports = { checkStatus, sendAlert };

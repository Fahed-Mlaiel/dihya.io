// monitoring.js – Monitoring, healthcheck
module.exports = {
  health: () => 'OK',
  metrics: () => ({ uptime: process.uptime() }),
};

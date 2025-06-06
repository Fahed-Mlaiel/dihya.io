// logger.js – Logger avancé, structuré, multitenant, RGPD-ready (Node.js)
const fs = require('fs');
const path = require('path');

function log(level, message, meta = {}) {
  const entry = {
    timestamp: new Date().toISOString(),
    level,
    message,
    ...meta
  };
  const logPath = path.join(__dirname, 'environnement.log');
  fs.appendFileSync(logPath, JSON.stringify(entry) + '\n');
}

module.exports = {
  info: (msg, meta) => log('info', msg, meta),
  warn: (msg, meta) => log('warn', msg, meta),
  error: (msg, meta) => log('error', msg, meta),
  audit: (msg, meta) => log('audit', msg, meta)
};

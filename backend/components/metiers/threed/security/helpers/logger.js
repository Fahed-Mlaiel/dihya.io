// logger.js – Logging sécurisé

function secureLog(message, level = 'INFO') {
  console.log(`[SECURE][${level}] ${message}`);
}

module.exports = { secureLog };

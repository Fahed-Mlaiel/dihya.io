// utils.js – Utilitaires sécurité

function maskSensitive(data) {
  if (typeof data !== 'string') return data;
  if (data.length <= 4) return '*'.repeat(data.length);
  return data.slice(0, 2) + '*'.repeat(data.length - 4) + data.slice(-2);
}

module.exports = { maskSensitive };

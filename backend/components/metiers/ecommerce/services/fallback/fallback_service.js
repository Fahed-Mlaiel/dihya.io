// fallback_service.js – Service fallback ultra avancé (clé en main)
function fallbackService(data) {
  if (!data) return { fallback: true, empty: true };
  return { ...data, fallback: true, status: 'fallback' };
}
module.exports = { fallbackService };

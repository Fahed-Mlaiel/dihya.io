// Mock RGPD avancé (anonymisation, export, consentement)
function anonymize(data) { return { ...data, secret: '***' }; }
function exportData(user, data) { return { user, export: JSON.stringify(data) }; }
function checkConsent(user) { if (!user) throw new Error('Consentement requis'); return true; }
module.exports = { anonymize, exportData, checkConsent };

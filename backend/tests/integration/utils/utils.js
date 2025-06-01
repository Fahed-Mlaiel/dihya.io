// Fonctions utilitaires avancées pour les tests d'intégration E2E Node.js
const jwt = require('jsonwebtoken');
const SECRET = process.env.JWT_SECRET || 'dihya_secret';

function getJwtTokenForRole(role) {
  return jwt.sign({ role, tenant: 'default', lang: 'fr' }, SECRET, { expiresIn: '1h' });
}

function mockI18n(lang = 'fr') {
  return { 'accept-language': lang };
}

function mockPlugin(name = 'seo') {
  return { name, enabled: true };
}

function mockAuditLog(module = 'test') {
  return { module, action: 'test', timestamp: new Date().toISOString() };
}

function mockFallbackIA(question = 'Test?', lang = 'fr') {
  return { answer: `Réponse IA (${lang}) à: ${question}` };
}

function mockSeoSitemap() {
  return '<urlset><url><loc>https://dihya.ai/</loc></url></urlset>';
}

module.exports = {
  getJwtTokenForRole,
  mockI18n,
  mockPlugin,
  mockAuditLog,
  mockFallbackIA,
  mockSeoSitemap
};

/**
 * @file utils.js
 * @description Utilitaires de test avancés pour les tests d'intégration Dihya (mocks, fixtures, JWT, audit, sécurité, i18n, RGPD, plugins, etc.)
 * @author Dihya
 * @date 2025-05-25
 */

const jwt = require('jsonwebtoken');

const SECRET = process.env.JWT_SECRET || 'test_secret';

function getTestToken(role = 'user') {
  return jwt.sign({ id: 1, role }, SECRET, { expiresIn: '1h' });
}

function setupTestDB() {
  // ... setup DB mocks/fixtures ...
  return Promise.resolve();
}

function teardownTestDB() {
  // ... teardown DB mocks/fixtures ...
  return Promise.resolve();
}

function mockRequest(data = {}) {
  return { ...data };
}

function mockResponse() {
  let statusCode = 200;
  let json;
  return {
    status(code) { statusCode = code; return this; },
    json(obj) { json = obj; return this; },
    get statusCode() { return statusCode; },
    _getJSON() { return json; }
  };
}

module.exports = {
  getTestToken,
  setupTestDB,
  teardownTestDB,
  mockRequest,
  mockResponse
};

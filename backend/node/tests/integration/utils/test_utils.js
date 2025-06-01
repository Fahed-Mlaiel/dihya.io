/**
 * @file test_utils.js
 * @description Tests unitaires et d'intégration pour les utilitaires de test (mocks, fixtures, audit, sécurité, i18n, RGPD, plugins, etc.)
 * @author Dihya
 * @date 2025-05-25
 */

const { setupTestDB, teardownTestDB, getTestToken, mockRequest, mockResponse } = require('./utils');

describe('Utils - Fonctions utilitaires avancées', () => {
  beforeAll(async () => { await setupTestDB(); });
  afterAll(async () => { await teardownTestDB(); });

  it('génère un token JWT valide pour chaque rôle', () => {
    expect(getTestToken('admin')).toMatch(/^ey/);
    expect(getTestToken('user')).toMatch(/^ey/);
    expect(getTestToken('guest')).toMatch(/^ey/);
  });

  it('mockRequest et mockResponse fonctionnent', () => {
    const req = mockRequest({ user: { id: 1, role: 'admin' } });
    const res = mockResponse();
    expect(req.user.role).toBe('admin');
    res.status(200).json({ ok: true });
    expect(res.statusCode).toBe(200);
    expect(res._getJSON()).toEqual({ ok: true });
  });

  it('setupTestDB et teardownTestDB ne lèvent pas d’erreur', async () => {
    await expect(setupTestDB()).resolves.not.toThrow();
    await expect(teardownTestDB()).resolves.not.toThrow();
  });
});

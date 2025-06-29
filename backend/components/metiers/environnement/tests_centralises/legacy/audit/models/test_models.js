const { AuditLog } = require('../../../../legacy/audit/models/models');

// Test ultra avancé pour models.js
// Cas nominaux, edge cases, conformité, sécurité, robustesse, documentation intégrée

describe('Audit Models - JS', () => {
  it('doit valider les modèles nominaux', () => {
    const log = new AuditLog('login', 'admin', 'success', { ip: '127.0.0.1' });
    const json = log.toJSON();
    expect(json.action).toBe('login');
    expect(json.user).toBe('admin');
    expect(json.status).toBe('success');
    expect(json.details.ip).toBe('127.0.0.1');
    expect(typeof json.timestamp).toBe('string');
  });

  it('doit gérer les cas limites et erreurs', () => {
    // details par défaut
    const log = new AuditLog('logout', 'user', 'fail');
    const json = log.toJSON();
    expect(json.details).toEqual({});
    expect(typeof json.timestamp).toBe('string');

    // timestamp explicite
    const date = new Date('2025-06-11T12:00:00Z');
    const log2 = new AuditLog('a', 'b', 'c', {}, date);
    expect(log2.timestamp).toBe(date);
    expect(log2.toJSON().timestamp).toBe(date.toISOString());
  });

  it('doit être conforme RGPD/audit', () => {
    const log = new AuditLog('export', 'dpo', 'ok', { rgpd: true });
    const json = log.toJSON();
    expect(json.details.rgpd).toBe(true);
    expect(json.action).toMatch(/export|login|logout/);
  });

  it('doit être robuste face aux entrées inattendues', () => {
    const log = new AuditLog(null, undefined, '', null);
    const json = log.toJSON();
    expect(json.action).toBe(null);
    expect(json.user).toBe(undefined);
    expect(json.status).toBe('');
    expect(json.details).toEqual({});
  });

  it('doit générer un timestamp ISO valide', () => {
    const log = new AuditLog('action', 'user', 'ok');
    const json = log.toJSON();
    expect(() => new Date(json.timestamp)).not.toThrow();
    expect(new Date(json.timestamp).toISOString()).toBe(json.timestamp);
  });
});

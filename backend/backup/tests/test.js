/**
 * @file Test d’intégration backup Dihya Coding (Node.js)
 * Sécurité, i18n, RGPD, plugins, audit, multitenancy, SEO, GraphQL, CI
 */
const assert = require('assert');
const request = require('supertest');
const express = require('express');
const backupService = require('../backup_service');
const { checkBackup, checkSecurity, checkMonitoring, checkGDPR, checkAccessibility, checkCI, checkPlugins, checkAudit } = require('../../utils/utils');

const app = express();
app.use(express.json());
app.use('/backup', backupService.router);

describe('Backup – Dihya Coding', () => {
  it('doit valider toutes les exigences de backup avancées', async () => {
    assert(await checkBackup());
    assert(await checkSecurity());
    assert(await checkMonitoring());
    assert(await checkGDPR());
    assert(await checkAccessibility());
    assert(await checkCI());
    assert(await checkPlugins());
    assert(await checkAudit());
  });

  it('doit valider la sauvegarde multilingue et la sécurité', async () => {
    // Mock JWT
    jest.spyOn(backupService, 'verify_jwt').mockImplementation(() => ({ sub: 'user456', role: 'admin' }));
    for (const [lang, expected] of Object.entries({ fr: 'Sauvegarde réussie', en: 'Backup successful', ar: 'تم النسخ الاحتياطي بنجاح' })) {
      const res = await request(app)
        .post('/backup')
        .set('Authorization', 'Bearer test.jwt.token')
        .set('Accept-Language', lang)
        .send({ project_id: 'proj123', user_id: 'user456', tenant_id: 'tenant789', options: { deep: true } });
      expect(res.statusCode).toBe(200);
      expect(res.body.message).toContain(expected);
    }
  });

  it('doit refuser un rôle non autorisé', async () => {
    jest.spyOn(backupService, 'verify_jwt').mockImplementation(() => ({ sub: 'user456', role: 'guest' }));
    const res = await request(app)
      .post('/backup')
      .set('Authorization', 'Bearer test.jwt.token')
      .set('Accept-Language', 'en')
      .send({ project_id: 'proj123', user_id: 'user456', tenant_id: 'tenant789', options: { deep: true } });
    expect(res.statusCode).toBe(403);
    expect(res.body.detail).toContain('Unauthorized');
  });

  it('doit refuser une requête invalide (body manquant)', async () => {
    jest.spyOn(backupService, 'verify_jwt').mockImplementation(() => ({ sub: 'user456', role: 'admin' }));
    const res = await request(app)
      .post('/backup')
      .set('Authorization', 'Bearer test.jwt.token')
      .set('Accept-Language', 'fr')
      .send({});
    expect(res.statusCode).toBe(400);
    expect(res.body.detail).toContain('invalide');
  });

  it('doit exposer le header SEO X-Robots-Tag', async () => {
    jest.spyOn(backupService, 'verify_jwt').mockImplementation(() => ({ sub: 'user456', role: 'admin' }));
    const res = await request(app)
      .post('/backup')
      .set('Authorization', 'Bearer test.jwt.token')
      .set('Accept-Language', 'en')
      .send({ project_id: 'proj123', user_id: 'user456' });
    expect(res.headers['x-robots-tag']).toBe('all');
  });

  it('doit permettre la sauvegarde via GraphQL', async () => {
    const mutation = `mutation { createBackup(project_id: \"p1\", user_id: \"u1\") { status message backup_id } }`;
    const res = await request(app)
      .post('/backup/graphql')
      .send({ query: mutation });
    expect(res.statusCode).toBe(200);
    expect(res.body.data.createBackup.status).toBe('success');
    expect(res.body.data.createBackup.message).toContain('Backup');
    expect(res.body.data.createBackup.backup_id).toMatch(/^backup_/);
  });
});

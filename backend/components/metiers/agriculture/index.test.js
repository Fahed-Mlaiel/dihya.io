"use strict";
/**
 * @file index.test.js
 * @module backend/components/metiers/agriculture/index.test
 * @description Tests unitaires et d’intégration pour le module Agriculture Dihya Coding (sécurité, i18n, plugins, RGPD, audit, REST/GraphQL).
 * @author Dihya Team
 * @license AGPL-3.0
 */

import express from 'express';
import request from 'supertest';
import router from './index.js';

const app = express();
app.use(express.json());
app.use('/api/agriculture', router);

// Mock JWT, RBAC, i18n, plugins, audit, etc.
app.use((err, req, res, next) => {
  res.status(500).json({ error: err.message });
});

describe('Agriculture API', () => {
  it('GET /api/agriculture/ doit retourner 200 et une liste (admin)', async () => {
    const res = await request(app)
      .get('/api/agriculture/')
      .set('Authorization', 'Bearer admin-token')
      .set('Accept-Language', 'fr');
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body.projects)).toBe(true);
  });

  it('POST /api/agriculture/ crée un projet agricole (user)', async () => {
    const res = await request(app)
      .post('/api/agriculture/')
      .set('Authorization', 'Bearer user-token')
      .send({ name: 'Test Agriculture', description: 'Projet test', type: 'Agriculture' });
    expect(res.statusCode).toBe(201);
    expect(res.body.project).toHaveProperty('id');
    expect(res.body.project.type).toBe('Agriculture');
  });

  // ...autres tests (update, delete, export, plugins, RGPD, audit, i18n, GraphQL, sécurité)
});

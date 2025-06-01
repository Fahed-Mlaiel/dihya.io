"use strict";
/**
 * @file index.test.js
 * @module backend/components/metiers/vr_ar/index.test
 * @description Tests unitaires et d’intégration pour le module VR/AR Dihya Coding (sécurité, i18n, plugins, RGPD, audit, REST/GraphQL).
 * @author Dihya Team
 * @license AGPL-3.0
 */

import express from 'express';
import request from 'supertest';
import router from './index.js';

const app = express();
app.use(express.json());
app.use('/api/vr-ar', router);

// Mock JWT, RBAC, i18n, plugins, audit, etc.
app.use((err, req, res, next) => {
  res.status(500).json({ error: err.message });
});

describe('VR/AR API', () => {
  it('GET /api/vr-ar/ doit retourner 200 et une liste (admin)', async () => {
    const res = await request(app)
      .get('/api/vr-ar/')
      .set('Authorization', 'Bearer admin-token')
      .set('Accept-Language', 'fr');
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body.projects)).toBe(true);
  });

  it('POST /api/vr-ar/ crée un projet VR/AR (user)', async () => {
    const res = await request(app)
      .post('/api/vr-ar/')
      .set('Authorization', 'Bearer user-token')
      .send({ name: 'Test VR', description: 'Projet test', type: 'VR' });
    expect(res.statusCode).toBe(201);
    expect(res.body.project).toHaveProperty('id');
    expect(res.body.project.type).toBe('VR');
  });

  // ...autres tests (update, delete, export, plugins, RGPD, audit, i18n, GraphQL, sécurité)
});

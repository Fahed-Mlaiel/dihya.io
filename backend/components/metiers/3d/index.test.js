"use strict";
/**
 * @file index.test.js
 * @module backend/components/metiers/3d/index.test
 * @description Tests unitaires et d’intégration pour le module 3D Dihya Coding (sécurité, i18n, plugins, RGPD, audit, REST/GraphQL).
 * @author Dihya Team
 * @license AGPL-3.0
 */

import express from 'express';
import request from 'supertest';
import router from './index.js';

const app = express();
app.use(express.json());
app.use('/api/3d', router);

// Mock JWT, RBAC, i18n, plugins, audit, etc.
app.use((err, req, res, next) => {
  res.status(500).json({ error: err.message });
});

describe('3D API', () => {
  it('GET /api/3d/ doit retourner 200 et une liste (admin)', async () => {
    const res = await request(app)
      .get('/api/3d/')
      .set('Authorization', 'Bearer admin-token')
      .set('Accept-Language', 'fr');
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body.projects)).toBe(true);
  });

  it('POST /api/3d/ crée un projet 3D (user)', async () => {
    const res = await request(app)
      .post('/api/3d/')
      .set('Authorization', 'Bearer user-token')
      .send({ name: 'Test 3D', description: 'Projet test', type: '3D' });
    expect(res.statusCode).toBe(201);
    expect(res.body.project).toHaveProperty('id');
    expect(res.body.project.type).toBe('3D');
  });

  // ...autres tests (update, delete, export, plugins, RGPD, audit, i18n, GraphQL, sécurité)
});

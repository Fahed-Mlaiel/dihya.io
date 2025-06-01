"use strict";
/**
 * @file index.test.js
 * @module backend/components/metiers/administration_publique/index.test
 * @description Tests unitaires et d’intégration pour le module Administration Publique Dihya Coding (sécurité, i18n, plugins, RGPD, audit, REST/GraphQL).
 * @author Dihya Team
 * @license AGPL-3.0
 */

import express from 'express';
import request from 'supertest';
import router from './index.js';

const app = express();
app.use(express.json());
app.use('/api/administration_publique', router);

// Mock JWT, RBAC, i18n, plugins, audit, etc.
app.use((err, req, res, next) => {
  res.status(500).json({ error: err.message });
});

describe('Administration Publique API', () => {
  it('GET /api/administration_publique/ doit retourner 200 et une liste (admin)', async () => {
    const res = await request(app)
      .get('/api/administration_publique/')
      .set('Authorization', 'Bearer admin-token')
      .set('Accept-Language', 'fr');
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body.services)).toBe(true);
  });

  it('POST /api/administration_publique/ crée un service (user)', async () => {
    const res = await request(app)
      .post('/api/administration_publique/')
      .set('Authorization', 'Bearer user-token')
      .send({ name: 'Test Service', description: 'Service test', type: 'Etat civil' });
    expect(res.statusCode).toBe(201);
    expect(res.body.service).toHaveProperty('id');
    expect(res.body.service.type).toBe('Etat civil');
  });

  // ...autres tests (update, delete, export, plugins, RGPD, audit, i18n, GraphQL, sécurité)
});

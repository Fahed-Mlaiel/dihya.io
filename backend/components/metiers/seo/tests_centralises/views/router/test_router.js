// test_router.js
// Tests avancés pour le module views/router (centralisation tests)
const request = require('supertest');
const express = require('express');
const router = require('../../../views/router/router');

describe('Views Router Central Tests', () => {
    let app;
    beforeAll(() => {
        app = express();
        app.use(express.json());
        app.use(router);
    });

    it('GET /seo retourne une liste vide', async () => {
        const res = await request(app).get('/seo');
        expect(res.status).toBe(200);
        expect(res.body).toEqual({ d3s: [], total: 0 });
    });

    it('POST /seo crée un objet seo avec valeurs par défaut', async () => {
        const res = await request(app).post('/seo').send({});
        expect(res.status).toBe(201);
        expect(res.body).toEqual({ nom: '', description: '', type: 'objet' });
    });

    it('POST /seo crée un objet seo avec données fournies', async () => {
        const data = { nom: 'Cube', description: 'Test', type: 'mesh' };
        const res = await request(app).post('/seo').send(data);
        expect(res.status).toBe(201);
        expect(res.body).toEqual(data);
    });

    it('POST /seo RGPD: ne retourne pas de données sensibles', async () => {
        const data = { nom: 'Cube', secret: 'should-not-leak' };
        const res = await request(app).post('/seo').send(data);
        expect(res.body).not.toHaveProperty('secret');
    });

    it('Accessibilité: toutes les routes répondent en JSON', async () => {
        const res = await request(app).get('/seo');
        expect(res.headers['content-type']).toMatch(/application\/json/);
    });
});

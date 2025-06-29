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

    it('GET /sport retourne une liste vide', async () => {
        const res = await request(app).get('/sport');
        expect(res.status).toBe(200);
        expect(res.body).toEqual({ d3s: [], total: 0 });
    });

    it('POST /sport crée un objet sport avec valeurs par défaut', async () => {
        const res = await request(app).post('/sport').send({});
        expect(res.status).toBe(201);
        expect(res.body).toEqual({ nom: '', description: '', type: 'objet' });
    });

    it('POST /sport crée un objet sport avec données fournies', async () => {
        const data = { nom: 'Cube', description: 'Test', type: 'mesh' };
        const res = await request(app).post('/sport').send(data);
        expect(res.status).toBe(201);
        expect(res.body).toEqual(data);
    });

    it('POST /sport RGPD: ne retourne pas de données sensibles', async () => {
        const data = { nom: 'Cube', secret: 'should-not-leak' };
        const res = await request(app).post('/sport').send(data);
        expect(res.body).not.toHaveProperty('secret');
    });

    it('Accessibilité: toutes les routes répondent en JSON', async () => {
        const res = await request(app).get('/sport');
        expect(res.headers['content-type']).toMatch(/application\/json/);
    });
});

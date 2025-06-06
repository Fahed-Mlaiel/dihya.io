// test_environnement_integration.js – Test d'intégration avancé Environnement (Node.js/Jest)
const request = require('supertest');
const app = require('../../index'); // Adapter selon l'entrée réelle de l'app

describe('Intégration Environnement', () => {
  it('cycle complet CRUD', async () => {
    // Création
    const create = await request(app).post('/environnements').send({ nom: 'Integration', description: 'desc', type: 'zone' });
    expect(create.statusCode).toBe(201);
    const id = create.body.id || 1;
    // Lecture
    const get = await request(app).get(`/environnements/${id}`);
    expect(get.statusCode).toBe(200);
    // Modification
    const update = await request(app).put(`/environnements/${id}`).send({ description: 'modifié' });
    expect(update.statusCode).toBe(200);
    // Suppression
    const del = await request(app).delete(`/environnements/${id}`);
    expect([200, 204]).toContain(del.statusCode);
  });
});

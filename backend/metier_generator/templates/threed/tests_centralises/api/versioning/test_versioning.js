// Tests ultra avancés du middleware de versioning API threed (Node.js)
const request = require('supertest');
const express = require('express');
const versioning = require('../../../../api/versioning/versioning');

describe('Versioning Middleware', () => {
  it('rejette une version non supportée', done => {
    const app = express();
    app.use(versioning);
    app.get('/v', (req, res) => res.json({ version: req.apiVersion }));
    request(app)
      .get('/v')
      .set('X-Api-Version', '42.0')
      .expect(400, done);
  });
  it('accepte une version supportée', done => {
    const app = express();
    app.use(versioning);
    app.get('/v', (req, res) => res.json({ version: req.apiVersion }));
    request(app)
      .get('/v')
      .set('X-Api-Version', '2.0')
      .expect(200)
      .expect(res => {
        expect(res.body.version).toBe('2.0');
      })
      .end(done);
  });
});

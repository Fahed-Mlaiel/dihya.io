const assert = require('assert');
const express = require('express');
const router = require('../../../api/core/api.js');

// Import basique ajouté automatiquement
// test_api.js – Tests ultra avancés pour api.py (API Video JS)

// TODO: Adapter ce test pour la logique JS équivalente à test_api.py

describe('API Video (Express router)', () => {
  it('should export a valid Express router', () => {
    expect(typeof router).toBe('function');
    // Vérifie que le router possède la méthode .use (signature Express)
    expect(typeof router.use).toBe('function');
    // Vérifie qu'il peut être monté sur une app Express
    const app = express();
    expect(() => app.use('/api/video', router)).not.toThrow();
  });
});

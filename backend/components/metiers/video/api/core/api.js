// api.js – Point d’entrée Express ultra avancé pour l’API Video
const express = require('express');
const router = express.Router();
const VideoController = require('../controllers/video_controller');
const { auditRequest, rgpdMiddleware, accessibilityMiddleware } = require('../middlewares/middlewares');
const { rgpdSanitize } = require('../rgpd/rgpd');
const { checkAccessibility } = require('../accessibility/accessibility');
const { auditEntity } = require('../audit/audit');
const { beforeAction, afterAction } = require('../hooks/hooks');

// Middleware RGPD, accessibilité, audit, logging
router.use(rgpdMiddleware);
router.use(accessibilityMiddleware);
router.use(auditRequest);

// GET video entity by ID
router.get('/video/:id', async (req, res) => {
  beforeAction('read', { id: req.params.id });
  try {
    let entity = await VideoController.getById(req.params.id);
    if (!entity) return res.status(404).json({ error: 'Not found' });
    entity = rgpdSanitize(entity);
    checkAccessibility(entity);
    auditEntity(entity, 'read');
    afterAction('read', entity);
    res.json(entity);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

// POST create video entity
router.post('/video', async (req, res) => {
  beforeAction('create', req.body);
  try {
    const created = await VideoController.create(req.body);
    auditEntity(created, 'create');
    afterAction('create', created);
    res.status(201).json(rgpdSanitize(created));
  } catch (e) {
    res.status(400).json({ error: e.message });
  }
});

// PUT update video entity
router.put('/video/:id', async (req, res) => {
  beforeAction('update', { id: req.params.id, ...req.body });
  try {
    const updated = await VideoController.update(req.params.id, req.body);
    auditEntity(updated, 'update');
    afterAction('update', updated);
    res.json(rgpdSanitize(updated));
  } catch (e) {
    res.status(400).json({ error: e.message });
  }
});

// DELETE video entity
router.delete('/video/:id', async (req, res) => {
  beforeAction('delete', { id: req.params.id });
  try {
    await VideoController.delete(req.params.id);
    auditEntity({ id: req.params.id }, 'delete');
    afterAction('delete', { id: req.params.id });
    res.status(204).end();
  } catch (e) {
    res.status(400).json({ error: e.message });
  }
});

// Gestion des edge cases, hooks, audit avancé, RGPD, accessibilité, documentation OpenAPI intégrée, etc.
// TODO: Ajouter routes avancées, gestion d’erreurs globales, synchronisation JS/Python, tests d’intégration multi-formats

module.exports = router;

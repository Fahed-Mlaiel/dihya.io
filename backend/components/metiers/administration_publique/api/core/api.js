// api.js – Point d’entrée Express ultra avancé pour l’API administration_publique
const express = require('express');
const router = express.Router();
const administration_publiqueController = require('../core/controllers/administration_publique_controller');
const { auditRequest, rgpdMiddleware, accessibilityMiddleware } = require('../core/middlewares/middlewares');
const { rgpdSanitize } = require('../core/rgpd/rgpd');
const { checkAccessibility } = require('../core/accessibility/accessibility');
const { auditEntity } = require('../core/audit/audit');
const { beforeAction, afterAction } = require('../core/hooks/hooks');

// Middleware RGPD, accessibilité, audit, logging
router.use(rgpdMiddleware);
router.use(accessibilityMiddleware);
router.use(auditRequest);

// GET administration_publique entity by ID
router.get('/administration_publique/:id', async (req, res) => {
  beforeAction('read', { id: req.params.id });
  try {
    let entity = await administration_publiqueController.getById(req.params.id);
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

// POST create administration_publique entity
router.post('/administration_publique', async (req, res) => {
  beforeAction('create', req.body);
  try {
    const created = await administration_publiqueController.create(req.body);
    auditEntity(created, 'create');
    afterAction('create', created);
    res.status(201).json(rgpdSanitize(created));
  } catch (e) {
    res.status(400).json({ error: e.message });
  }
});

// PUT update administration_publique entity
router.put('/administration_publique/:id', async (req, res) => {
  beforeAction('update', { id: req.params.id, ...req.body });
  try {
    const updated = await administration_publiqueController.update(req.params.id, req.body);
    auditEntity(updated, 'update');
    afterAction('update', updated);
    res.json(rgpdSanitize(updated));
  } catch (e) {
    res.status(400).json({ error: e.message });
  }
});

// DELETE administration_publique entity
router.delete('/administration_publique/:id', async (req, res) => {
  beforeAction('delete', { id: req.params.id });
  try {
    await administration_publiqueController.delete(req.params.id);
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

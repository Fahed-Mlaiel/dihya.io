// api.js – Point d’entrée Express ultra avancé pour l’API Ressources_humaines
const express = require('express');
const router = express.Router();
const Ressources_humainesController = require('../core/controllers/ressources_humaines_controller');
const { auditRequest, rgpdMiddleware, accessibilityMiddleware } = require('../core/middlewares/middlewares');
const { rgpdSanitize } = require('../core/rgpd/rgpd');
const { checkAccessibility } = require('../core/accessibility/accessibility');
const { auditEntity } = require('../core/audit/audit');
const { beforeAction, afterAction } = require('../core/hooks/hooks');

// Middleware RGPD, accessibilité, audit, logging
router.use(rgpdMiddleware);
router.use(accessibilityMiddleware);
router.use(auditRequest);

// GET ressources_humaines entity by ID
router.get('/ressources_humaines/:id', async (req, res) => {
  beforeAction('read', { id: req.params.id });
  try {
    let entity = await Ressources_humainesController.getById(req.params.id);
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

// POST create ressources_humaines entity
router.post('/ressources_humaines', async (req, res) => {
  beforeAction('create', req.body);
  try {
    const created = await Ressources_humainesController.create(req.body);
    auditEntity(created, 'create');
    afterAction('create', created);
    res.status(201).json(rgpdSanitize(created));
  } catch (e) {
    res.status(400).json({ error: e.message });
  }
});

// PUT update ressources_humaines entity
router.put('/ressources_humaines/:id', async (req, res) => {
  beforeAction('update', { id: req.params.id, ...req.body });
  try {
    const updated = await Ressources_humainesController.update(req.params.id, req.body);
    auditEntity(updated, 'update');
    afterAction('update', updated);
    res.json(rgpdSanitize(updated));
  } catch (e) {
    res.status(400).json({ error: e.message });
  }
});

// DELETE ressources_humaines entity
router.delete('/ressources_humaines/:id', async (req, res) => {
  beforeAction('delete', { id: req.params.id });
  try {
    await Ressources_humainesController.delete(req.params.id);
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

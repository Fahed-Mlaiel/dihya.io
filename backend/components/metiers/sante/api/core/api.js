// api.js – Point d’entrée Express ultra avancé pour l’API Sante
const express = require('express');
const router = express.Router();
const SanteController = require('../core/controllers/sante_controller');
const { auditRequest, rgpdMiddleware, accessibilityMiddleware } = require('../core/middlewares/middlewares');
const { rgpdSanitize } = require('../core/rgpd/rgpd');
const { checkAccessibility } = require('../core/accessibility/accessibility');
const { auditEntity } = require('../core/audit/audit');
const { beforeAction, afterAction } = require('../core/hooks/hooks');

// Middleware RGPD, accessibilité, audit, logging
router.use(rgpdMiddleware);
router.use(accessibilityMiddleware);
router.use(auditRequest);

// GET sante entity by ID
router.get('/sante/:id', async (req, res) => {
  beforeAction('read', { id: req.params.id });
  try {
    let entity = await SanteController.getById(req.params.id);
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

// POST create sante entity
router.post('/sante', async (req, res) => {
  beforeAction('create', req.body);
  try {
    const created = await SanteController.create(req.body);
    auditEntity(created, 'create');
    afterAction('create', created);
    res.status(201).json(rgpdSanitize(created));
  } catch (e) {
    res.status(400).json({ error: e.message });
  }
});

// PUT update sante entity
router.put('/sante/:id', async (req, res) => {
  beforeAction('update', { id: req.params.id, ...req.body });
  try {
    const updated = await SanteController.update(req.params.id, req.body);
    auditEntity(updated, 'update');
    afterAction('update', updated);
    res.json(rgpdSanitize(updated));
  } catch (e) {
    res.status(400).json({ error: e.message });
  }
});

// DELETE sante entity
router.delete('/sante/:id', async (req, res) => {
  beforeAction('delete', { id: req.params.id });
  try {
    await SanteController.delete(req.params.id);
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

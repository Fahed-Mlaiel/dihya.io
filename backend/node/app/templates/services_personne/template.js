/**
 * Template RESTful pour la gestion avancée de projets services à la personne (IA, VR, AR, etc.)
 * Sécurité maximale, multilingue, multitenant, extensible, RGPD, SEO, plugins, audit, tests.
 * @module services_personne/template
 * @author Dihya Coding
 * @version 1.0.0
 * @license MIT
 */

const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, validateBody } = require('../../../../middlewares/security');
const { servicesPersonneSchema } = require('./validation');
const router = express.Router();

/**
 * @swagger
 * tags:
 *   name: ServicesPersonne
 *   description: API pour la gestion de projets services à la personne (IA, VR, AR...)
 */

router.use(i18nMiddleware);
router.use(auditLog);

router.get('/', checkJwt, checkRole(['admin', 'user']), async (req, res) => {
  res.status(200).json([{ id: 1, nom: req.t('Exemple Service à la personne') }]);
});

router.post('/', checkJwt, checkRole(['admin']), validateBody(servicesPersonneSchema), async (req, res) => {
  res.status(201).json({ id: 2, ...req.body });
});

// ... autres routes (PUT, DELETE, GraphQL, plugins, IA fallback)

module.exports = router;

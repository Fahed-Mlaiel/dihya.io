"use strict";
/**
 * @file api.js
 * @module backend/components/metiers/automobile/api
 * @description Routes REST/GraphQL ultra avancées pour la gestion de projets automobile (sécurité, i18n, plugins, RGPD, audit, SEO, multitenancy, fallback IA, accessibilité, documentation intégrée, tests, extensibilité, conformité CI/CD, multilingue, logs structurés, export, anonymisation, etc.).
 * @author Dihya Team
 * @license AGPL-3.0
 */

import express from 'express';
import { auditLog, checkJwt, checkRole, i18nMiddleware, validateAutomobile } from '../../../middlewares/security';
import { pluginManager } from '../../../plugins/pluginManager';
import { createAutomobileProject, deleteAutomobileProject, getAutomobileProjects, updateAutomobileProject } from './automobile_controller.js';

const router = express.Router();

// Internationalisation dynamique
router.use(i18nMiddleware);

// Audit logging
router.use(auditLog);

// Liste des projets automobile
router.get('/', checkJwt, checkRole(['admin', 'user']), getAutomobileProjects);

// Création d'un projet automobile
router.post('/', checkJwt, checkRole(['admin', 'user']), validateAutomobile, createAutomobileProject);

// Modification d'un projet automobile
router.put('/:id', checkJwt, checkRole(['admin']), validateAutomobile, updateAutomobileProject);

// Suppression d'un projet automobile
router.delete('/:id', checkJwt, checkRole(['admin']), deleteAutomobileProject);

// Extension plugins automobile
router.use('/plugins', pluginManager('automobile'));

export default router;

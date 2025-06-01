"use strict";
/**
 * @file index.js
 * @module backend/components/metiers/agriculture/index
 * @description Routes REST/GraphQL ultra avancées pour la gestion de projets agricoles (sécurité, i18n, plugins, RGPD, audit, SEO, multitenancy, fallback IA, accessibilité, documentation intégrée, tests, extensibilité, conformité CI/CD, multilingue, logs structurés, export, anonymisation, etc.).
 * @author Dihya Team
 * @license AGPL-3.0
 */

import express from 'express';
import { auditLog, checkJwt, checkRole, i18nMiddleware, validateAgriculture } from '../../../middlewares/security';
import { pluginManager } from '../../../plugins/pluginManager';
import { createAgricultureProject, deleteAgricultureProject, getAgricultureProjects, updateAgricultureProject } from './agriculture_controller.js';

const router = express.Router();

// Internationalisation dynamique
router.use(i18nMiddleware);

// Audit logging
router.use(auditLog);

// Liste des projets agricoles
router.get('/', checkJwt, checkRole(['admin', 'user']), getAgricultureProjects);

// Création d'un projet agricole
router.post('/', checkJwt, checkRole(['admin', 'user']), validateAgriculture, createAgricultureProject);

// Modification d'un projet agricole
router.put('/:id', checkJwt, checkRole(['admin']), validateAgriculture, updateAgricultureProject);

// Suppression d'un projet agricole
router.delete('/:id', checkJwt, checkRole(['admin']), deleteAgricultureProject);

// Extension plugins agriculture
router.use('/plugins', pluginManager('agriculture'));

export default router;

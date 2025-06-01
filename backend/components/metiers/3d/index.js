"use strict";
/**
 * @file index.js
 * @module backend/components/metiers/3d/index
 * @description Routes REST/GraphQL ultra avancées pour la gestion de projets 3D (sécurité, i18n, plugins, RGPD, audit, SEO, multitenancy, fallback IA, accessibilité, documentation intégrée, tests, extensibilité, conformité CI/CD, multilingue, logs structurés, export, anonymisation, etc.).
 * @author Dihya Team
 * @license AGPL-3.0
 */

import express from 'express';
import { auditLog, checkJwt, checkRole, i18nMiddleware, validate3D } from '../../../middlewares/security';
import { pluginManager } from '../../../plugins/pluginManager';
import { create3DProject, delete3DProject, get3DProjects, update3DProject } from './three_controller.js';

const router = express.Router();

// Internationalisation dynamique
router.use(i18nMiddleware);

// Audit logging
router.use(auditLog);

// Liste des projets 3D
router.get('/', checkJwt, checkRole(['admin', 'user']), get3DProjects);

// Création d'un projet 3D
router.post('/', checkJwt, checkRole(['admin', 'user']), validate3D, create3DProject);

// Modification d'un projet 3D
router.put('/:id', checkJwt, checkRole(['admin']), validate3D, update3DProject);

// Suppression d'un projet 3D
router.delete('/:id', checkJwt, checkRole(['admin']), delete3DProject);

// Extension plugins 3D
router.use('/plugins', pluginManager('3d'));

export default router;

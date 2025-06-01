"use strict";
/**
 * @file index.js
 * @module backend/components/metiers/arts/index
 * @description Routes REST/GraphQL ultra avancées pour la gestion de projets artistiques (sécurité, i18n, plugins, RGPD, audit, SEO, multitenancy, fallback IA, accessibilité, documentation intégrée, tests, extensibilité, conformité CI/CD, multilingue, logs structurés, export, anonymisation, etc.).
 * @author Dihya Team
 * @license AGPL-3.0
 */

import express from 'express';
import { auditLog, checkJwt, checkRole, i18nMiddleware, validateArts } from '../../../middlewares/security';
import { pluginManager } from '../../../plugins/pluginManager';
import { createArtsProject, deleteArtsProject, getArtsProjects, updateArtsProject } from './arts_controller.js';

const router = express.Router();

// Internationalisation dynamique
router.use(i18nMiddleware);

// Audit logging
router.use(auditLog);

// Liste des projets artistiques
router.get('/', checkJwt, checkRole(['admin', 'user']), getArtsProjects);

// Création d'un projet artistique
router.post('/', checkJwt, checkRole(['admin', 'user']), validateArts, createArtsProject);

// Modification d'un projet artistique
router.put('/:id', checkJwt, checkRole(['admin']), validateArts, updateArtsProject);

// Suppression d'un projet artistique
router.delete('/:id', checkJwt, checkRole(['admin']), deleteArtsProject);

// Extension plugins arts
router.use('/plugins', pluginManager('arts'));

export default router;

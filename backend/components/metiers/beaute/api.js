"use strict";
/**
 * @file api.js
 * @module backend/components/metiers/beaute/api
 * @description Routes REST/GraphQL ultra avancées pour la gestion de projets beauté (sécurité, i18n, plugins, RGPD, audit, SEO, multitenancy, fallback IA, accessibilité, documentation intégrée, tests, extensibilité, conformité CI/CD, multilingue, logs structurés, export, anonymisation, etc.).
 * @author Dihya Team
 * @license AGPL-3.0
 */

import express from 'express';
import { auditLog, checkJwt, checkRole, i18nMiddleware, validateBeaute } from '../../../middlewares/security';
import { pluginManager } from '../../../plugins/pluginManager';
import { createBeauteProject, deleteBeauteProject, getBeauteProjects, updateBeauteProject } from './beaute_controller.js';

const router = express.Router();

// Internationalisation dynamique
router.use(i18nMiddleware);

// Audit logging
router.use(auditLog);

// Liste des projets beauté
router.get('/', checkJwt, checkRole(['admin', 'user']), getBeauteProjects);

// Création d'un projet beauté
router.post('/', checkJwt, checkRole(['admin', 'user']), validateBeaute, createBeauteProject);

// Modification d'un projet beauté
router.put('/:id', checkJwt, checkRole(['admin']), validateBeaute, updateBeauteProject);

// Suppression d'un projet beauté
router.delete('/:id', checkJwt, checkRole(['admin']), deleteBeauteProject);

// Extension plugins beauté
router.use('/plugins', pluginManager('beaute'));

export default router;

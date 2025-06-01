"use strict";
/**
 * @file api.js
 * @module backend/components/metiers/assurance/api
 * @description Routes REST/GraphQL ultra avancées pour la gestion de projets assurance (sécurité, i18n, plugins, RGPD, audit, SEO, multitenancy, fallback IA, accessibilité, documentation intégrée, tests, extensibilité, conformité CI/CD, multilingue, logs structurés, export, anonymisation, etc.).
 * @author Dihya Team
 * @license AGPL-3.0
 */

import express from 'express';
import { auditLog, checkJwt, checkRole, i18nMiddleware, validateAssurance } from '../../../middlewares/security';
import { pluginManager } from '../../../plugins/pluginManager';
import { createAssuranceProject, deleteAssuranceProject, getAssuranceProjects, updateAssuranceProject } from './assurance_controller.js';

const router = express.Router();

// Internationalisation dynamique
router.use(i18nMiddleware);

// Audit logging
router.use(auditLog);

// Liste des projets assurance
router.get('/', checkJwt, checkRole(['admin', 'user']), getAssuranceProjects);

// Création d'un projet assurance
router.post('/', checkJwt, checkRole(['admin', 'user']), validateAssurance, createAssuranceProject);

// Modification d'un projet assurance
router.put('/:id', checkJwt, checkRole(['admin']), validateAssurance, updateAssuranceProject);

// Suppression d'un projet assurance
router.delete('/:id', checkJwt, checkRole(['admin']), deleteAssuranceProject);

// Extension plugins assurance
router.use('/plugins', pluginManager('assurance'));

export default router;

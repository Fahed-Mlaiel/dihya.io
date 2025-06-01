"use strict";
/**
 * @file index.js
 * @module backend/components/metiers/administration_publique/index
 * @description Routes REST/GraphQL ultra avancées pour la gestion de services d'administration publique (sécurité, i18n, plugins, RGPD, audit, SEO, multitenancy, fallback IA, accessibilité, documentation intégrée, tests, extensibilité, conformité CI/CD, multilingue, logs structurés, export, anonymisation, etc.).
 * @author Dihya Team
 * @license AGPL-3.0
 */

import express from 'express';
import { auditLog, checkJwt, checkRole, i18nMiddleware, validateAdminService } from '../../../middlewares/security';
import { pluginManager } from '../../../plugins/pluginManager';
import { createAdminService, deleteAdminService, getAdminServices, updateAdminService } from './admin_controller.js';

const router = express.Router();

// Internationalisation dynamique
router.use(i18nMiddleware);

// Audit logging
router.use(auditLog);

// Liste des services d'administration publique
router.get('/', checkJwt, checkRole(['admin', 'user']), getAdminServices);

// Création d'un service
router.post('/', checkJwt, checkRole(['admin', 'user']), validateAdminService, createAdminService);

// Modification d'un service
router.put('/:id', checkJwt, checkRole(['admin']), validateAdminService, updateAdminService);

// Suppression d'un service
router.delete('/:id', checkJwt, checkRole(['admin']), deleteAdminService);

// Extension plugins administration publique
router.use('/plugins', pluginManager('administration_publique'));

export default router;

"use strict";
/**
 * @file api.js
 * @module backend/components/metiers/banque_finance/api
 * @description Routes REST/GraphQL ultra avancées pour la gestion de projets banque/finance (sécurité, i18n, plugins, RGPD, audit, SEO, multitenancy, fallback IA, accessibilité, documentation intégrée, tests, extensibilité, conformité CI/CD, multilingue, logs structurés, export, anonymisation, etc.).
 * @author Dihya Team
 * @license AGPL-3.0
 */

import express from 'express';
import { auditLog, checkJwt, checkRole, i18nMiddleware, validateBanqueFinance } from '../../../middlewares/security';
import { pluginManager } from '../../../plugins/pluginManager';
import { createBanqueFinanceProject, deleteBanqueFinanceProject, getBanqueFinanceProjects, updateBanqueFinanceProject } from './banque_finance_controller.js';

const router = express.Router();

// Internationalisation dynamique
router.use(i18nMiddleware);

// Audit logging
router.use(auditLog);

// Liste des projets banque/finance
router.get('/', checkJwt, checkRole(['admin', 'user']), getBanqueFinanceProjects);

// Création d'un projet banque/finance
router.post('/', checkJwt, checkRole(['admin', 'user']), validateBanqueFinance, createBanqueFinanceProject);

// Modification d'un projet banque/finance
router.put('/:id', checkJwt, checkRole(['admin']), validateBanqueFinance, updateBanqueFinanceProject);

// Suppression d'un projet banque/finance
router.delete('/:id', checkJwt, checkRole(['admin']), deleteBanqueFinanceProject);

// Extension plugins banque/finance
router.use('/plugins', pluginManager('banque_finance'));

export default router;

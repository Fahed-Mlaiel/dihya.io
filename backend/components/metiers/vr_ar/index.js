// src/components/metiers/vr_ar/index.js
/**
 * Gestion avancée des routes VR/AR pour Dihya Coding
 * Sécurité maximale, internationalisation, multitenancy, plugins, RGPD, audit, IA fallback
 * @module src/components/metiers/vr_ar/index.js
 */
import express from 'express';
import { auditLog, checkJwt, checkRole, i18nMiddleware, validateVRAR } from '../../../middlewares/security';
import { pluginManager } from '../../../plugins/pluginManager';
import { createVRARProject, deleteVRARProject, getVRARProjects, updateVRARProject } from './vra_controller';

const router = express.Router();

// Internationalisation dynamique
router.use(i18nMiddleware);

// Audit logging
router.use(auditLog);

// Liste des projets VR/AR
router.get('/', checkJwt, checkRole(['admin', 'user']), getVRARProjects);

// Création d'un projet VR/AR
router.post('/', checkJwt, checkRole(['admin', 'user']), validateVRAR, createVRARProject);

// Modification d'un projet VR/AR
router.put('/:id', checkJwt, checkRole(['admin']), validateVRAR, updateVRARProject);

// Suppression d'un projet VR/AR
router.delete('/:id', checkJwt, checkRole(['admin']), deleteVRARProject);

// Extension plugins VR/AR
router.use('/plugins', pluginManager('vr_ar'));

export default router;

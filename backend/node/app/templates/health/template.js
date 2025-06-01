// Template de routes santé avancé (REST, GraphQL, sécurité, i18n, plugins, RGPD, SEO, multitenancy, audit, IA, tests)
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, pluginLoader } = require('../../../../core/middleware');
const { getRecords, createAppointment, updateAppointment, deleteAppointment } = require('./controller');
const router = express.Router();

router.use(i18nMiddleware);
router.use(checkJwt);
router.use(auditLog);
router.use(pluginLoader);

/**
 * @route GET /health/records
 * @desc Liste des dossiers médicaux (multi-tenant, filtrage, pagination, i18n)
 * @access Roles: admin, médecin, patient, invité
 */
router.get('/records', checkRole(['admin', 'doctor', 'patient', 'guest']), getRecords);

/**
 * @route POST /health/appointment
 * @desc Prise de rendez-vous (validation, audit, RGPD)
 * @access Roles: admin, médecin, patient
 */
router.post('/appointment', checkRole(['admin', 'doctor', 'patient']), createAppointment);

/**
 * @route PUT /health/appointment/:id
 * @desc Mise à jour d'un rendez-vous
 * @access Roles: admin, médecin
 */
router.put('/appointment/:id', checkRole(['admin', 'doctor']), updateAppointment);

/**
 * @route DELETE /health/appointment/:id
 * @desc Suppression d'un rendez-vous (audit, anonymisation RGPD)
 * @access Roles: admin
 */
router.delete('/appointment/:id', checkRole(['admin']), deleteAppointment);

module.exports = router;

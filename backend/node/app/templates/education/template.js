// Template de routes éducation avancé (REST, GraphQL, sécurité, i18n, plugins, RGPD, SEO, multitenancy, audit, IA, tests)
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, pluginLoader } = require('../../../../core/middleware');
const { getCourses, enrollCourse, updateCourse, deleteCourse } = require('./controller');
const router = express.Router();

router.use(i18nMiddleware);
router.use(checkJwt);
router.use(auditLog);
router.use(pluginLoader);

/**
 * @route GET /education/courses
 * @desc Liste des cours (multi-tenant, filtrage, pagination, i18n)
 * @access Roles: admin, teacher, student, guest
 */
router.get('/courses', checkRole(['admin', 'teacher', 'student', 'guest']), getCourses);

/**
 * @route POST /education/enroll
 * @desc Inscription à un cours (validation, audit, RGPD)
 * @access Roles: admin, teacher, student
 */
router.post('/enroll', checkRole(['admin', 'teacher', 'student']), enrollCourse);

/**
 * @route PUT /education/courses/:id
 * @desc Mise à jour d'un cours
 * @access Roles: admin, teacher
 */
router.put('/courses/:id', checkRole(['admin', 'teacher']), updateCourse);

/**
 * @route DELETE /education/courses/:id
 * @desc Suppression d'un cours (audit, anonymisation RGPD)
 * @access Roles: admin
 */
router.delete('/courses/:id', checkRole(['admin']), deleteCourse);

module.exports = router;

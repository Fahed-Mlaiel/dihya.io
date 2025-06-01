"""
Template de routes e-commerce avancé (REST, GraphQL, sécurité, i18n, plugins, RGPD, SEO, multitenancy, audit, IA, tests)
"""
const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLog, pluginLoader } = require('../../../../core/middleware');
const { getProducts, createOrder, updateOrder, deleteOrder } = require('./controller');
const router = express.Router();

router.use(i18nMiddleware);
router.use(checkJwt);
router.use(auditLog);
router.use(pluginLoader);

/**
 * @route GET /ecommerce/products
 * @desc Liste des produits (multi-tenant, filtrage, pagination, i18n)
 * @access Roles: admin, user, invité
 */
router.get('/products', checkRole(['admin', 'user', 'guest']), getProducts);

/**
 * @route POST /ecommerce/orders
 * @desc Création d'une commande (validation, audit, RGPD)
 * @access Roles: admin, user
 */
router.post('/orders', checkRole(['admin', 'user']), createOrder);

/**
 * @route PUT /ecommerce/orders/:id
 * @desc Mise à jour d'une commande
 * @access Roles: admin, user
 */
router.put('/orders/:id', checkRole(['admin', 'user']), updateOrder);

/**
 * @route DELETE /ecommerce/orders/:id
 * @desc Suppression d'une commande (audit, anonymisation RGPD)
 * @access Roles: admin
 */
router.delete('/orders/:id', checkRole(['admin']), deleteOrder);

module.exports = router;

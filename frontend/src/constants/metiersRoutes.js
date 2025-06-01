// metiersRoutes.js - Routes métiers Dihya Coding
/**
 * @fileoverview Définition des routes métiers (REST, GraphQL, sécurité, rôles, i18n)
 * @author Dihya Coding
 * @version 1.0.0
 * @license MIT
 */

export const METIERS_ROUTES = [
  {
    path: '/metiers/voyage',
    component: 'Voyage',
    roles: ['admin', 'user'],
    i18n: true,
    rest: true,
    graphql: true
  },
  {
    path: '/metiers/vr_ar',
    component: 'VRAR',
    roles: ['admin', 'user'],
    i18n: true,
    rest: true,
    graphql: true
  },
  // ...autres routes métiers
];

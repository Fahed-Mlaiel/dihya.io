// users.js - mocks avancés pour tests unitaires, multitenant, rôles, RGPD
/**
 * @file users.js
 * @description Fixtures utilisateurs pour tests avancés (admin, user, invité, RGPD, anonymisation)
 * @i18n (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
 * @roles (admin, user, invité)
 * @audit (logs, anonymisation, export)
 */

export const mockAdmin = {
  id: 'admin-1',
  username: 'admin',
  email: 'admin@dihya.io',
  role: 'admin',
  tenant: 'dihya',
  isActive: true,
  isAnonymized: false
};

export const mockUser = {
  id: 'user-1',
  username: 'user',
  email: 'user@dihya.io',
  role: 'user',
  tenant: 'dihya',
  isActive: true,
  isAnonymized: false
};

export const mockGuest = {
  id: 'guest-1',
  username: 'guest',
  email: 'guest@dihya.io',
  role: 'guest',
  tenant: 'dihya',
  isActive: true,
  isAnonymized: false
};

export const anonymizedUser = {
  ...mockUser,
  email: null,
  username: 'anonymized',
  isAnonymized: true
};

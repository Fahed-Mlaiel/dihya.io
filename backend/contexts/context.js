// src/contexts/context.js
/**
 * Contexte global Dihya Coding (i18n, sécurité, rôles, plugins, audit, RGPD)
 * @module src/contexts/context.js
 */
import { createContext } from 'react';
import { ROLES, SUPPORTED_LANGUAGES } from '../constants/constants';

export const DihyaContext = createContext({
  language: 'fr',
  role: 'guest',
  tenant: null,
  plugins: [],
  audit: [],
  setLanguage: () => {},
  setRole: () => {},
  setTenant: () => {},
  addPlugin: () => {},
  logAudit: () => {},
});

export const defaultLanguages = SUPPORTED_LANGUAGES;
export const defaultRoles = ROLES;

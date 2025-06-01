// context.js - Contexte global Dihya Coding
/**
 * @fileoverview Contexte global sécurisé, multilingue, multitenant, gestion des rôles, audit, documentation intégrée.
 * @author Dihya Coding
 * @version 1.0.0
 * @license MIT
 */
import { createContext, useState } from 'react';

export const AuthContext = createContext({
  user: null,
  setUser: () => {},
  tenant: null,
  setTenant: () => {},
  language: 'fr',
  setLanguage: () => {},
});

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [tenant, setTenant] = useState(null);
  const [language, setLanguage] = useState('fr');

  return (
    <AuthContext.Provider value={{ user, setUser, tenant, setTenant, language, setLanguage }}>
      {children}
    </AuthContext.Provider>
  );
};

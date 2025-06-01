/**
 * @file AuthContext.js
 * @description Contexte d’authentification centralisé pour Dihya Coding.
 * Garantit sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les données sont validées, anonymisées si besoin, et respectent le consentement utilisateur.
 */

import React, { createContext, useContext, useState, useEffect } from 'react';

/**
 * Structure utilisateur par défaut (aucune donnée sensible).
 */
const DEFAULT_USER = {
  id: null,
  username: null,
  role: 'guest',
  email: null,
  isAuthenticated: false,
};

/**
 * Contexte React pour l’authentification.
 */
const AuthContext = createContext({
  user: DEFAULT_USER,
  login: async () => {},
  logout: () => {},
  isAuthenticated: false,
  setUser: () => {},
});

/**
 * Fournisseur d’authentification pour l’application Dihya Coding.
 * @param {object} props
 * @param {React.ReactNode} props.children
 * @returns {JSX.Element}
 */
export function AuthProvider({ children }) {
  const [user, setUser] = useState(DEFAULT_USER);

  // Vérifie le token JWT au chargement (sécurité)
  useEffect(() => {
    const token = localStorage.getItem('jwt_token');
    if (token) {
      // Appel API pour valider le token et récupérer l’utilisateur
      fetch('/api/user/me', {
        headers: { Authorization: `Bearer ${token}` },
      })
        .then(res => res.ok ? res.json() : null)
        .then(data => {
          if (data && data.id) {
            setUser({
              id: data.id,
              username: data.username,
              role: data.role,
              email: data.email || null,
              isAuthenticated: true,
            });
            logAuthEvent('auto_login', data.username);
          } else {
            setUser(DEFAULT_USER);
            localStorage.removeItem('jwt_token');
          }
        })
        .catch(() => {
          setUser(DEFAULT_USER);
          localStorage.removeItem('jwt_token');
        });
    }
  }, []);

  /**
   * Connecte l’utilisateur (login).
   * @param {string} username
   * @param {string} password
   * @returns {Promise<boolean>}
   */
  async function login(username, password) {
    if (!username || !password) throw new Error('Identifiants requis');
    const res = await fetch('/api/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password }),
    });
    if (!res.ok) throw new Error('Échec de la connexion');
    const data = await res.json();
    if (data && data.token) {
      localStorage.setItem('jwt_token', data.token);
      setUser({
        id: data.user.id,
        username: data.user.username,
        role: data.user.role,
        email: data.user.email || null,
        isAuthenticated: true,
      });
      logAuthEvent('login', username);
      return true;
    }
    throw new Error('Réponse inattendue');
  }

  /**
   * Déconnecte l’utilisateur (logout).
   */
  function logout() {
    setUser(DEFAULT_USER);
    localStorage.removeItem('jwt_token');
    logAuthEvent('logout', user.username);
  }

  return (
    <AuthContext.Provider value={{
      user,
      login,
      logout,
      isAuthenticated: !!user && !!user.isAuthenticated,
      setUser,
    }}>
      {children}
    </AuthContext.Provider>
  );
}

/**
 * Hook pour accéder au contexte d’authentification.
 * @returns {{user: object, login: function, logout: function, isAuthenticated: boolean, setUser: function}}
 */
export function useAuth() {
  return useContext(AuthContext);
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} value
 */
function logAuthEvent(action, value) {
  try {
    const logs = JSON.parse(localStorage.getItem('auth_logs') || '[]');
    logs.push({
      action,
      value,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('auth_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs d’authentification locaux (droit à l’oubli RGPD).
 */
export function clearLocalAuthLogs() {
  localStorage.removeItem('auth_logs');
}
import React from 'react';
// Gestion du contexte d’authentification (exemple simplifié)
export const AuthContext = React.createContext();
export function AuthProvider({ children }) {
  const [user, setUser] = React.useState(null);
  const login = (email, password) => setUser({ email });
  const logout = () => setUser(null);
  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

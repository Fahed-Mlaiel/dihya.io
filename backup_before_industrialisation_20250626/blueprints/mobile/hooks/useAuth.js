import { useState, useEffect } from 'react';
export function useAuth() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) { setUser({ name: 'Admin', role: 'admin', token }); }
    setLoading(false);
  }, []);
  const login = async (email, password) => {
    if (email === 'admin@dihya.io' && password === 'azerty') {
      const fakeToken = 'jwt.token.exemple';
      localStorage.setItem('token', fakeToken);
      setUser({ name: 'Admin', role: 'admin', token: fakeToken });
      return true;
    }
    return false;
  };
  const logout = () => { localStorage.removeItem('token'); setUser(null); };
  return { user, loading, login, logout };
}
import React, { useState } from 'react';
// Formulaire d’inscription avancé avec validation et gestion d’erreur
export default function RegisterForm({ onRegister }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const handleSubmit = (e) => {
    e.preventDefault();
    if (!email || !password) return setError('Tous les champs sont obligatoires');
    setError(null);
    onRegister && onRegister(email, password);
  };
  return (
    <form onSubmit={handleSubmit}>
      <input value={email} onChange={e=>setEmail(e.target.value)} placeholder='Email' />
      <input type='password' value={password} onChange={e=>setPassword(e.target.value)} placeholder='Mot de passe' />
      <button type='submit'>Inscription</button>
      {error && <div style={{color:'red'}}>{error}</div>}
    </form>
  );
}

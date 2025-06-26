import React, { useState } from 'react';
// Formulaire de modification des paramètres utilisateur
export default function UserSettings({ user, onSave }) {
  const [name, setName] = useState(user?.name || '');
  const [email, setEmail] = useState(user?.email || '');
  return (
    <form onSubmit={e => {e.preventDefault();onSave && onSave({ name, email });}}>
      <input value={name} onChange={e=>setName(e.target.value)} placeholder='Nom' />
      <input value={email} onChange={e=>setEmail(e.target.value)} placeholder='Email' />
      <button type='submit'>Enregistrer</button>
    </form>
  );
}

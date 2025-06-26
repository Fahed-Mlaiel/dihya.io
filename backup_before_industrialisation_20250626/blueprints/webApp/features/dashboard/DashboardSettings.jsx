import React, { useState } from 'react';
// Paramètres du dashboard utilisateur
export default function DashboardSettings({ settings, onSave }) {
  const [notif, setNotif] = useState(settings?.notif ?? true);
  return (
    <form onSubmit={e => {e.preventDefault();onSave && onSave({ notif });}}>
      <label>
        <input type='checkbox' checked={notif} onChange={e=>setNotif(e.target.checked)} /> Notifications
      </label>
      <button type='submit'>Enregistrer</button>
    </form>
  );
}

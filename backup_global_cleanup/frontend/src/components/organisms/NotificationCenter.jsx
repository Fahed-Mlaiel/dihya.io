import React from 'react';
// Organism NotificationCenter avancé
export default function NotificationCenter({ notifications, onClear }) {
  return (
    <aside className='notification-center'>
      <h4>Notifications</h4>
      <ul>
        {notifications.map((n, i) => <li key={i}>{n.message}</li>)}
      </ul>
      <button onClick={onClear}>Tout effacer</button>
    </aside>
  );
}

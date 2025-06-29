import React from 'react';
// Atom Switch avancé
export default function Switch({ checked, onChange, label }) {
  return (
    <label className='switch'>
      <input type='checkbox' checked={checked} onChange={e=>onChange(e.target.checked)} />
      <span className='slider'></span>
      {label && <span>{label}</span>}
    </label>
  );
}

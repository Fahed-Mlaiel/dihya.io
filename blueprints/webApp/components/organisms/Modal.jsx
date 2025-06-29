import React from 'react';
// Organism Modal avancé
export default function Modal({ open, onClose, children }) {
  if (!open) return null;
  return (
    <div className='modal'>
      <div className='modal-content'>
        <button className='modal-close' onClick={onClose}>×</button>
        {children}
      </div>
    </div>
  );
}

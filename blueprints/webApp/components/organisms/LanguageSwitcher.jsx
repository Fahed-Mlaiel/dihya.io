import React from 'react';
export default function LanguageSwitcher({ onChange, lang }) {
  return (
    <select onChange={onChange} value={lang} className='lang-switcher'>
      <option value='fr'>FR</option>
      <option value='en'>EN</option>
      <option value='ar'>AR</option>
      <option value='ber'>BER</option>
    </select>
  );
}

// LangContext.js
// Contexte global pour la gestion de la langue (i18n)
import React, { createContext, useContext, useState } from 'react';

const LangContext = createContext();

export function LangProvider({ children }) {
  const [lang, setLang] = useState('fr');
  const changeLang = (newLang) => setLang(newLang);
  return (
    <LangContext.Provider value={{ lang, changeLang }}>
      {children}
    </LangContext.Provider>
  );
}

export function useLang() {
  return useContext(LangContext);
}

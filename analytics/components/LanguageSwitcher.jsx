import React, { useState, useEffect } from 'react';
import i18n from 'i18next';
import { useTranslation } from 'react-i18next';
import { trackEvent } from '../analytics'; // Supposons que cette fonction envoie des événements analytics

const LanguageSwitcher = () => {
  const { t } = useTranslation();
  const [language, setLanguage] = useState(i18n.language);

  useEffect(() => {
    i18n.changeLanguage(language);
    trackEvent('language_change', { language });
  }, [language]);

  const handleLanguageChange = (event) => {
    setLanguage(event.target.value);
  };

  return (
    <select
      aria-label={t('languageSwitcher.ariaLabel')}
      onChange={handleLanguageChange}
      value={language}
    >
      <option value="en">{t('languageSwitcher.english')}</option>
      <option value="fr">{t('languageSwitcher.french')}</option>
      <option value="es">{t('languageSwitcher.spanish')}</option>
      {/* Ajouter d'autres options de langue selon les besoins */}
    </select>
  );
};

export default LanguageSwitcher;
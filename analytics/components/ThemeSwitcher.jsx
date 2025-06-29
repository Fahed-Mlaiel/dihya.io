import React, { useContext, useEffect } from 'react';
import { ThemeContext } from '../context/ThemeContext';
import { trackEvent } from '../analytics';
import { useTranslation } from 'react-i18next';

const ThemeSwitcher = () => {
  const { t } = useTranslation();
  const { theme, toggleTheme } = useContext(ThemeContext);

  useEffect(() => {
    // Track the theme change event for analytics
    trackEvent('theme_change', {
      theme: theme,
    });
  }, [theme]);

  const handleThemeChange = () => {
    toggleTheme();
    // Track the theme toggle event for analytics
    trackEvent('theme_toggle', {
      from: theme,
      to: theme === 'light' ? 'dark' : 'light',
    });
  };

  return (
    <button onClick={handleThemeChange} aria-label={t('themeSwitcher.ariaLabel')}>
      {theme === 'light' ? t('themeSwitcher.darkMode') : t('themeSwitcher.lightMode')}
    </button>
  );
};

export default ThemeSwitcher;
import PropTypes from 'prop-types';
import React from 'react';
import { useTranslation } from 'react-i18next';

/**
 * Dashboard Énergie – gestion production, IA, optimisation, sécurité.
 * @param {string} userRole - Rôle utilisateur (admin, user, invité)
 * @param {string} lang - Langue d’interface (fr, en, ar, ...)
 */
function EnergieDashboard({ userRole, lang }) {
  const { t, i18n } = useTranslation();
  React.useEffect(() => { i18n.changeLanguage(lang); }, [lang, i18n]);
  return (
    <section aria-label={t('energie.dashboard')}>
      <h1>{t('energie.title')}</h1>
      {/* Composants production, IA, optimisation, sécurité, etc. */}
      {userRole === 'admin' && <button>{t('energie.adminPanel')}</button>}
    </section>
  );
}
EnergieDashboard.propTypes = {
  userRole: PropTypes.oneOf(['admin', 'user', 'invité']).isRequired,
  lang: PropTypes.string.isRequired,
};
export default EnergieDashboard;

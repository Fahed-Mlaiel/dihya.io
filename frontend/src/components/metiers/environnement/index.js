import PropTypes from 'prop-types';
import React from 'react';
import { useTranslation } from 'react-i18next';

/**
 * Dashboard Environnement – gestion suivi, conformité, IA, VR.
 * @param {string} userRole - Rôle utilisateur (admin, user, invité)
 * @param {string} lang - Langue d’interface (fr, en, ar, ...)
 */
function EnvironnementDashboard({ userRole, lang }) {
  const { t, i18n } = useTranslation();
  React.useEffect(() => { i18n.changeLanguage(lang); }, [lang, i18n]);
  return (
    <section aria-label={t('environnement.dashboard')}>
      <h1>{t('environnement.title')}</h1>
      {/* Composants suivi, conformité, IA, VR, etc. */}
      {userRole === 'admin' && <button>{t('environnement.adminPanel')}</button>}
    </section>
  );
}
EnvironnementDashboard.propTypes = {
  userRole: PropTypes.oneOf(['admin', 'user', 'invité']).isRequired,
  lang: PropTypes.string.isRequired,
};
export default EnvironnementDashboard;

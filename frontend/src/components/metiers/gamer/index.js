import PropTypes from 'prop-types';
import React from 'react';
import { useTranslation } from 'react-i18next';

/**
 * Dashboard Gamer – gestion communautés, tournois, IA, VR.
 * @param {string} userRole - Rôle utilisateur (admin, user, invité)
 * @param {string} lang - Langue d’interface (fr, en, ar, ...)
 */
function GamerDashboard({ userRole, lang }) {
  const { t, i18n } = useTranslation();
  React.useEffect(() => { i18n.changeLanguage(lang); }, [lang, i18n]);
  return (
    <section aria-label={t('gamer.dashboard')}>
      <h1>{t('gamer.title')}</h1>
      {/* Composants communautés, tournois, IA, VR, etc. */}
      {userRole === 'admin' && <button>{t('gamer.adminPanel')}</button>}
    </section>
  );
}
GamerDashboard.propTypes = {
  userRole: PropTypes.oneOf(['admin', 'user', 'invité']).isRequired,
  lang: PropTypes.string.isRequired,
};
export default GamerDashboard;

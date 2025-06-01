import PropTypes from 'prop-types';
import React from 'react';
import { useTranslation } from 'react-i18next';

/**
 * Dashboard Culture – gestion événements, patrimoine, IA, VR.
 * @param {string} userRole - Rôle utilisateur (admin, user, invité)
 * @param {string} lang - Langue d’interface (fr, en, ar, ...)
 */
function CultureDashboard({ userRole, lang }) {
  const { t, i18n } = useTranslation();
  React.useEffect(() => { i18n.changeLanguage(lang); }, [lang, i18n]);
  return (
    <section aria-label={t('culture.dashboard')}>
      <h1>{t('culture.title')}</h1>
      {/* Composants événements, patrimoine, IA, VR, etc. */}
      {userRole === 'admin' && <button>{t('culture.adminPanel')}</button>}
    </section>
  );
}
CultureDashboard.propTypes = {
  userRole: PropTypes.oneOf(['admin', 'user', 'invité']).isRequired,
  lang: PropTypes.string.isRequired,
};
export default CultureDashboard;

import PropTypes from 'prop-types';
import React from 'react';
import { useTranslation } from 'react-i18next';

/**
 * Dashboard Construction – gestion projets, IA, sécurité.
 * @param {string} userRole - Rôle utilisateur (admin, user, invité)
 * @param {string} lang - Langue d’interface (fr, en, ar, ...)
 */
function ConstructionDashboard({ userRole, lang }) {
  const { t, i18n } = useTranslation();
  React.useEffect(() => { i18n.changeLanguage(lang); }, [lang, i18n]);
  return (
    <section aria-label={t('construction.dashboard')}>
      <h1>{t('construction.title')}</h1>
      {/* Composants gestion projets, IA, sécurité, etc. */}
      {userRole === 'admin' && <button>{t('construction.adminPanel')}</button>}
    </section>
  );
}
ConstructionDashboard.propTypes = {
  userRole: PropTypes.oneOf(['admin', 'user', 'invité']).isRequired,
  lang: PropTypes.string.isRequired,
};
export default ConstructionDashboard;

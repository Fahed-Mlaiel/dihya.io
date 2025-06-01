import PropTypes from 'prop-types';
import React from 'react';
import { useTranslation } from 'react-i18next';

/**
 * Dashboard Éducation – gestion cours, IA, VR, sécurité.
 * @param {string} userRole - Rôle utilisateur (admin, user, invité)
 * @param {string} lang - Langue d’interface (fr, en, ar, ...)
 */
function EducationDashboard({ userRole, lang }) {
  const { t, i18n } = useTranslation();
  React.useEffect(() => { i18n.changeLanguage(lang); }, [lang, i18n]);
  return (
    <section aria-label={t('education.dashboard')}>
      <h1>{t('education.title')}</h1>
      {/* Composants cours, IA, VR, sécurité, etc. */}
      {userRole === 'admin' && <button>{t('education.adminPanel')}</button>}
    </section>
  );
}
EducationDashboard.propTypes = {
  userRole: PropTypes.oneOf(['admin', 'user', 'invité']).isRequired,
  lang: PropTypes.string.isRequired,
};
export default EducationDashboard;

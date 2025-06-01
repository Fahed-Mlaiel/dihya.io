import PropTypes from 'prop-types';
import React from 'react';
import { useTranslation } from 'react-i18next';

/**
 * Dashboard BTP – gestion chantiers, IA, sécurité, BIM.
 * @param {string} userRole - Rôle utilisateur (admin, user, invité)
 * @param {string} lang - Langue d’interface (fr, en, ar, ...)
 */
function BtpDashboard({ userRole, lang }) {
  const { t, i18n } = useTranslation();
  React.useEffect(() => { i18n.changeLanguage(lang); }, [lang, i18n]);
  return (
    <section aria-label={t('btp.dashboard')}>
      <h1>{t('btp.title')}</h1>
      {/* Composants gestion chantiers, IA, sécurité, BIM, etc. */}
      {userRole === 'admin' && <button>{t('btp.adminPanel')}</button>}
    </section>
  );
}
BtpDashboard.propTypes = {
  userRole: PropTypes.oneOf(['admin', 'user', 'invité']).isRequired,
  lang: PropTypes.string.isRequired,
};
export default BtpDashboard;

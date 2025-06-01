import PropTypes from 'prop-types';
import React from 'react';
import { useTranslation } from 'react-i18next';

/**
 * Dashboard Crypto – gestion wallets, trading, IA, sécurité.
 * @param {string} userRole - Rôle utilisateur (admin, user, invité)
 * @param {string} lang - Langue d’interface (fr, en, ar, ...)
 */
function CryptoDashboard({ userRole, lang }) {
  const { t, i18n } = useTranslation();
  React.useEffect(() => { i18n.changeLanguage(lang); }, [lang, i18n]);
  return (
    <section aria-label={t('crypto.dashboard')}>
      <h1>{t('crypto.title')}</h1>
      {/* Composants wallets, trading, IA, sécurité, etc. */}
      {userRole === 'admin' && <button>{t('crypto.adminPanel')}</button>}
    </section>
  );
}
CryptoDashboard.propTypes = {
  userRole: PropTypes.oneOf(['admin', 'user', 'invité']).isRequired,
  lang: PropTypes.string.isRequired,
};
export default CryptoDashboard;

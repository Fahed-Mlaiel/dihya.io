import PropTypes from 'prop-types';
import React from 'react';
import { useTranslation } from 'react-i18next';

/**
 * Dashboard Blockchain – gestion wallets, NFT, IA, sécurité.
 * @param {string} userRole - Rôle utilisateur (admin, user, invité)
 * @param {string} lang - Langue d’interface (fr, en, ar, ...)
 */
function BlockchainDashboard({ userRole, lang }) {
  const { t, i18n } = useTranslation();
  React.useEffect(() => { i18n.changeLanguage(lang); }, [lang, i18n]);
  return (
    <section aria-label={t('blockchain.dashboard')}>
      <h1>{t('blockchain.title')}</h1>
      {/* Composants wallets, NFT, IA, sécurité, etc. */}
      {userRole === 'admin' && <button>{t('blockchain.adminPanel')}</button>}
    </section>
  );
}
BlockchainDashboard.propTypes = {
  userRole: PropTypes.oneOf(['admin', 'user', 'invité']).isRequired,
  lang: PropTypes.string.isRequired,
};
export default BlockchainDashboard;

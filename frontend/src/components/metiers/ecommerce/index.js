import PropTypes from 'prop-types';
import React from 'react';
import { useTranslation } from 'react-i18next';

/**
 * Dashboard E-commerce – gestion produits, commandes, IA, SEO.
 * @param {string} userRole - Rôle utilisateur (admin, user, invité)
 * @param {string} lang - Langue d’interface (fr, en, ar, ...)
 */
function EcommerceDashboard({ userRole, lang }) {
  const { t, i18n } = useTranslation();
  React.useEffect(() => { i18n.changeLanguage(lang); }, [lang, i18n]);
  return (
    <section aria-label={t('ecommerce.dashboard')}>
      <h1>{t('ecommerce.title')}</h1>
      {/* Composants produits, commandes, IA, SEO, etc. */}
      {userRole === 'admin' && <button>{t('ecommerce.adminPanel')}</button>}
    </section>
  );
}
EcommerceDashboard.propTypes = {
  userRole: PropTypes.oneOf(['admin', 'user', 'invité']).isRequired,
  lang: PropTypes.string.isRequired,
};
export default EcommerceDashboard;

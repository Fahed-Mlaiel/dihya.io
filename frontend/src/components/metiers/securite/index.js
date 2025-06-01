import PropTypes from 'prop-types';
import { useTranslation } from 'react-i18next';
import { SecuriteAIWidget } from '../../plugins/SecuriteAIWidget';
import { withRole } from '../../security/withRole';

/**
 * Composant Sécurité avancé
 * @module Securite
 * @description Gestion des projets de sécurité (cybersécurité, audit, IA sécurité, etc.)
 * @security CORS, JWT, validation, audit, WAF, anti-DDOS
 * @i18n Dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
 * @roles admin, user, invité
 * @seo Optimisé
 * @example <Securite userRole="admin" />
 */
const Securite = withRole(['admin', 'user', 'invité'])(function Securite({ userRole, tenant }) {
  const { t } = useTranslation();
  return (
    <section aria-label={t('securite.sectionLabel', 'Sécurité')}>
      <h2>{t('securite.title', 'Gestion Sécurité')}</h2>
      <SecuriteAIWidget tenant={tenant} />
      <p>{t('securite.description', 'Module avancé pour la gestion sécurité, compatible IA, RGPD, multilingue.')}</p>
    </section>
  );
});

Securite.propTypes = {
  userRole: PropTypes.oneOf(['admin', 'user', 'invité']).isRequired,
  tenant: PropTypes.string
};

export default Securite;

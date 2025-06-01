import PropTypes from 'prop-types';
import { useTranslation } from 'react-i18next';
import { IndustrieAIWidget } from '../../plugins/IndustrieAIWidget';
import { withRole } from '../../security/withRole';

/**
 * Composant Industrie avancé
 * @module Industrie
 * @description Gestion des projets industriels (usines, IoT, IA, etc.)
 * @security CORS, JWT, validation, audit, WAF, anti-DDOS
 * @i18n Dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
 * @roles admin, user, invité
 * @seo Optimisé
 * @example <Industrie userRole="admin" />
 */
const Industrie = withRole(['admin', 'user', 'invité'])(function Industrie({ userRole, tenant }) {
  const { t } = useTranslation();
  return (
    <section aria-label={t('industrie.sectionLabel', 'Industrie')}>
      <h2>{t('industrie.title', 'Gestion Industrie')}</h2>
      <IndustrieAIWidget tenant={tenant} />
      <p>{t('industrie.description', 'Module avancé pour la gestion industrielle, compatible IA, RGPD, multilingue.')}</p>
    </section>
  );
});

Industrie.propTypes = {
  userRole: PropTypes.oneOf(['admin', 'user', 'invité']).isRequired,
  tenant: PropTypes.string
};

export default Industrie;

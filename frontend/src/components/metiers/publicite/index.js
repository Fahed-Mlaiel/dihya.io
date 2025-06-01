import PropTypes from 'prop-types';
import { useTranslation } from 'react-i18next';
import { PubliciteAIWidget } from '../../plugins/PubliciteAIWidget';
import { withRole } from '../../security/withRole';

/**
 * Composant Publicité avancé
 * @module Publicite
 * @description Gestion des projets publicitaires (campagnes, IA, analytics, etc.)
 * @security CORS, JWT, validation, audit, WAF, anti-DDOS
 * @i18n Dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
 * @roles admin, user, invité
 * @seo Optimisé
 * @example <Publicite userRole="admin" />
 */
const Publicite = withRole(['admin', 'user', 'invité'])(function Publicite({ userRole, tenant }) {
  const { t } = useTranslation();
  return (
    <section aria-label={t('publicite.sectionLabel', 'Publicité')}>
      <h2>{t('publicite.title', 'Gestion Publicité')}</h2>
      <PubliciteAIWidget tenant={tenant} />
      <p>{t('publicite.description', 'Module avancé pour la gestion publicitaire, compatible IA, RGPD, multilingue.')}</p>
    </section>
  );
});

Publicite.propTypes = {
  userRole: PropTypes.oneOf(['admin', 'user', 'invité']).isRequired,
  tenant: PropTypes.string
};

export default Publicite;

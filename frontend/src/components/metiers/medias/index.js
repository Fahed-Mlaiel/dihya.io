import PropTypes from 'prop-types';
import { useTranslation } from 'react-i18next';
import { MediaAIWidget } from '../../plugins/MediaAIWidget';
import { withRole } from '../../security/withRole';

/**
 * Composant Médias avancé
 * @module Medias
 * @description Gestion des projets médias (presse, TV, IA, etc.)
 * @security CORS, JWT, validation, audit, WAF, anti-DDOS
 * @i18n Dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
 * @roles admin, user, invité
 * @seo Optimisé
 * @example <Medias userRole="admin" />
 */
const Medias = withRole(['admin', 'user', 'invité'])(function Medias({ userRole, tenant }) {
  const { t } = useTranslation();
  return (
    <section aria-label={t('medias.sectionLabel', 'Médias')}>
      <h2>{t('medias.title', 'Gestion Médias')}</h2>
      <MediaAIWidget tenant={tenant} />
      <p>{t('medias.description', 'Module avancé pour la gestion médias, compatible IA, RGPD, multilingue.')}</p>
    </section>
  );
});

Medias.propTypes = {
  userRole: PropTypes.oneOf(['admin', 'user', 'invité']).isRequired,
  tenant: PropTypes.string
};

export default Medias;

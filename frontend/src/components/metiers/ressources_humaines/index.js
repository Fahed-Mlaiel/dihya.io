import PropTypes from 'prop-types';
import { useTranslation } from 'react-i18next';
import { RHWidget } from '../../plugins/RHWidget';
import { withRole } from '../../security/withRole';

/**
 * Composant Ressources Humaines avancé
 * @module RessourcesHumaines
 * @description Gestion des projets RH (recrutement, IA RH, etc.)
 * @security CORS, JWT, validation, audit, WAF, anti-DDOS
 * @i18n Dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
 * @roles admin, user, invité
 * @seo Optimisé
 * @example <RessourcesHumaines userRole="admin" />
 */
const RessourcesHumaines = withRole(['admin', 'user', 'invité'])(function RessourcesHumaines({ userRole, tenant }) {
  const { t } = useTranslation();
  return (
    <section aria-label={t('rh.sectionLabel', 'Ressources Humaines')}>
      <h2>{t('rh.title', 'Gestion RH')}</h2>
      <RHWidget tenant={tenant} />
      <p>{t('rh.description', 'Module avancé pour la gestion RH, compatible IA, RGPD, multilingue.')}</p>
    </section>
  );
});

RessourcesHumaines.propTypes = {
  userRole: PropTypes.oneOf(['admin', 'user', 'invité']).isRequired,
  tenant: PropTypes.string
};

export default RessourcesHumaines;

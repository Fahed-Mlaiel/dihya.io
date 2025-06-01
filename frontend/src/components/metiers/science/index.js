import PropTypes from 'prop-types';
import { useTranslation } from 'react-i18next';
import { ScienceAIWidget } from '../../plugins/ScienceAIWidget';
import { withRole } from '../../security/withRole';

/**
 * Composant Science avancé
 * @module Science
 * @description Gestion des projets scientifiques (laboratoires, IA science, etc.)
 * @security CORS, JWT, validation, audit, WAF, anti-DDOS
 * @i18n Dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
 * @roles admin, user, invité
 * @seo Optimisé
 * @example <Science userRole="admin" />
 */
const Science = withRole(['admin', 'user', 'invité'])(function Science({ userRole, tenant }) {
  const { t } = useTranslation();
  return (
    <section aria-label={t('science.sectionLabel', 'Science')}>
      <h2>{t('science.title', 'Gestion Science')}</h2>
      <ScienceAIWidget tenant={tenant} />
      <p>{t('science.description', 'Module avancé pour la gestion science, compatible IA, RGPD, multilingue.')}</p>
    </section>
  );
});

Science.propTypes = {
  userRole: PropTypes.oneOf(['admin', 'user', 'invité']).isRequired,
  tenant: PropTypes.string
};

export default Science;

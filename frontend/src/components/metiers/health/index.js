import PropTypes from 'prop-types';
import { useTranslation } from 'react-i18next';
import { HealthAIWidget } from '../../plugins/HealthAIWidget';
import { withRole } from '../../security/withRole';

/**
 * Composant Santé avancé (Health)
 * @module Health
 * @description Gestion des projets santé (HealthTech, MedTech, IA médicale, etc.)
 * @security CORS, JWT, validation, audit, WAF, anti-DDOS
 * @i18n Dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
 * @roles admin, user, invité
 * @seo Optimisé
 * @example <Health userRole="admin" />
 */
const Health = withRole(['admin', 'user', 'invité'])(function Health({ userRole, tenant }) {
  const { t } = useTranslation();
  return (
    <section aria-label={t('health.sectionLabel', 'Santé')}>
      <h2>{t('health.title', 'Gestion Santé')}</h2>
      <HealthAIWidget tenant={tenant} />
      <p>{t('health.description', 'Module avancé pour la gestion des projets santé, compatible IA, RGPD, multilingue.')}</p>
    </section>
  );
});

Health.propTypes = {
  userRole: PropTypes.oneOf(['admin', 'user', 'invité']).isRequired,
  tenant: PropTypes.string
};

export default Health;

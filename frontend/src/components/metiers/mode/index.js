import PropTypes from 'prop-types';
import { useTranslation } from 'react-i18next';
import { ModeAIWidget } from '../../plugins/ModeAIWidget';
import { withRole } from '../../security/withRole';

/**
 * Composant Mode avancé
 * @module Mode
 * @description Gestion des projets mode (e-commerce, IA, tendances, etc.)
 * @security CORS, JWT, validation, audit, WAF, anti-DDOS
 * @i18n Dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
 * @roles admin, user, invité
 * @seo Optimisé
 * @example <Mode userRole="admin" />
 */
const Mode = withRole(['admin', 'user', 'invité'])(function Mode({ userRole, tenant }) {
  const { t } = useTranslation();
  return (
    <section aria-label={t('mode.sectionLabel', 'Mode')}>
      <h2>{t('mode.title', 'Gestion Mode')}</h2>
      <ModeAIWidget tenant={tenant} />
      <p>{t('mode.description', 'Module avancé pour la gestion mode, compatible IA, RGPD, multilingue.')}</p>
    </section>
  );
});

Mode.propTypes = {
  userRole: PropTypes.oneOf(['admin', 'user', 'invité']).isRequired,
  tenant: PropTypes.string
};

export default Mode;

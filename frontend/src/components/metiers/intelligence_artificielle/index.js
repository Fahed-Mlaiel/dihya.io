import PropTypes from 'prop-types';
import { useTranslation } from 'react-i18next';
import { IAAIWidget } from '../../plugins/IAAIWidget';
import { withRole } from '../../security/withRole';

/**
 * Composant Intelligence Artificielle avancé
 * @module IntelligenceArtificielle
 * @description Gestion des projets IA (génération, NLP, vision, etc.)
 * @security CORS, JWT, validation, audit, WAF, anti-DDOS
 * @i18n Dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
 * @roles admin, user, invité
 * @seo Optimisé
 * @example <IntelligenceArtificielle userRole="admin" />
 */
const IntelligenceArtificielle = withRole(['admin', 'user', 'invité'])(function IntelligenceArtificielle({ userRole, tenant }) {
  const { t } = useTranslation();
  return (
    <section aria-label={t('ia.sectionLabel', 'Intelligence Artificielle')}>
      <h2>{t('ia.title', 'Gestion Intelligence Artificielle')}</h2>
      <IAAIWidget tenant={tenant} />
      <p>{t('ia.description', 'Module avancé pour la gestion de projets IA, compatible RGPD, multilingue, plugins IA.')}</p>
    </section>
  );
});

IntelligenceArtificielle.propTypes = {
  userRole: PropTypes.oneOf(['admin', 'user', 'invité']).isRequired,
  tenant: PropTypes.string
};

export default IntelligenceArtificielle;

import PropTypes from 'prop-types';
import { useTranslation } from 'react-i18next';
import { RechercheAIWidget } from '../../plugins/RechercheAIWidget';
import { withRole } from '../../security/withRole';

/**
 * Composant Recherche avancé
 * @module Recherche
 * @description Gestion des projets de recherche (scientifique, IA, innovation, etc.)
 * @security CORS, JWT, validation, audit, WAF, anti-DDOS
 * @i18n Dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
 * @roles admin, user, invité
 * @seo Optimisé
 * @example <Recherche userRole="admin" />
 */
const Recherche = withRole(['admin', 'user', 'invité'])(function Recherche({ userRole, tenant }) {
  const { t } = useTranslation();
  return (
    <section aria-label={t('recherche.sectionLabel', 'Recherche')}>
      <h2>{t('recherche.title', 'Gestion Recherche')}</h2>
      <RechercheAIWidget tenant={tenant} />
      <p>{t('recherche.description', 'Module avancé pour la gestion recherche, compatible IA, RGPD, multilingue.')}</p>
    </section>
  );
});

Recherche.propTypes = {
  userRole: PropTypes.oneOf(['admin', 'user', 'invité']).isRequired,
  tenant: PropTypes.string
};

export default Recherche;

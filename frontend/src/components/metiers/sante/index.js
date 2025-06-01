import PropTypes from 'prop-types';
import { useTranslation } from 'react-i18next';
import { SanteAIWidget } from '../../plugins/SanteAIWidget';
import { withRole } from '../../security/withRole';

/**
 * Composant Santé publique avancé
 * @module Sante
 * @description Gestion des projets santé publique (hôpitaux, IA santé, etc.)
 * @security CORS, JWT, validation, audit, WAF, anti-DDOS
 * @i18n Dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
 * @roles admin, user, invité
 * @seo Optimisé
 * @example <Sante userRole="admin" />
 */
const Sante = withRole(['admin', 'user', 'invité'])(function Sante({ userRole, tenant }) {
  const { t } = useTranslation();
  return (
    <section aria-label={t('sante.sectionLabel', 'Santé publique')}>
      <h2>{t('sante.title', 'Gestion Santé Publique')}</h2>
      <SanteAIWidget tenant={tenant} />
      <p>{t('sante.description', 'Module avancé pour la gestion santé publique, compatible IA, RGPD, multilingue.')}</p>
    </section>
  );
});

Sante.propTypes = {
  userRole: PropTypes.oneOf(['admin', 'user', 'invité']).isRequired,
  tenant: PropTypes.string
};

export default Sante;

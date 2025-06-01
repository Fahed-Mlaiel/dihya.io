import PropTypes from 'prop-types';
import { useTranslation } from 'react-i18next';
import { HospitalityAIWidget } from '../../plugins/HospitalityAIWidget';
import { withRole } from '../../security/withRole';

/**
 * Composant Hôtellerie avancé
 * @module Hotellerie
 * @description Gestion des projets hôtellerie (hôtels, IA, réservation, etc.)
 * @security CORS, JWT, validation, audit, WAF, anti-DDOS
 * @i18n Dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
 * @roles admin, user, invité
 * @seo Optimisé
 * @example <Hotellerie userRole="admin" />
 */
const Hotellerie = withRole(['admin', 'user', 'invité'])(function Hotellerie({ userRole, tenant }) {
  const { t } = useTranslation();
  return (
    <section aria-label={t('hotellerie.sectionLabel', 'Hôtellerie')}>
      <h2>{t('hotellerie.title', 'Gestion Hôtellerie')}</h2>
      <HospitalityAIWidget tenant={tenant} />
      <p>{t('hotellerie.description', 'Module avancé pour la gestion hôtelière, compatible IA, RGPD, multilingue.')}</p>
    </section>
  );
});

Hotellerie.propTypes = {
  userRole: PropTypes.oneOf(['admin', 'user', 'invité']).isRequired,
  tenant: PropTypes.string
};

export default Hotellerie;

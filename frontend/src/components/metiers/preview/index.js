import PropTypes from 'prop-types';
import { useTranslation } from 'react-i18next';
import { PreviewAIWidget } from '../../plugins/PreviewAIWidget';
import { withRole } from '../../security/withRole';

/**
 * Composant Preview avancé
 * @module Preview
 * @description Aperçu dynamique de projets métiers (IA, VR, AR, web, mobile, etc.)
 * @security CORS, JWT, validation, audit, WAF, anti-DDOS
 * @i18n Dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
 * @roles admin, user, invité
 * @seo Optimisé
 * @example <Preview userRole="admin" />
 */
const Preview = withRole(['admin', 'user', 'invité'])(function Preview({ userRole, tenant }) {
  const { t } = useTranslation();
  return (
    <section aria-label={t('preview.sectionLabel', 'Aperçu')}>
      <h2>{t('preview.title', 'Aperçu Dynamique')}</h2>
      <PreviewAIWidget tenant={tenant} />
      <p>{t('preview.description', 'Module avancé pour l’aperçu dynamique de projets métiers, compatible IA, RGPD, multilingue.')}</p>
    </section>
  );
});

Preview.propTypes = {
  userRole: PropTypes.oneOf(['admin', 'user', 'invité']).isRequired,
  tenant: PropTypes.string
};

export default Preview;

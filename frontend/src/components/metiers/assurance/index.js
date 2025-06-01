// Composant Assurance – Dihya Frontend
// Gestion des contrats, sinistres, IA, sécurité, i18n, plugins, RGPD
// Compatible Codespaces/Linux/CI

import PropTypes from 'prop-types';

/**
 * Composant Assurance
 * @param {string} userRole - Rôle utilisateur (admin, user, invité)
 * @param {string} lang - Langue (fr, en, ar, ...)
 * @param {object} [plugin] - Plugin métier optionnel
 */
export function Assurance({ userRole, lang, plugin }) {
  // Sécurité, i18n, audit, plugins
  // ...
  return (
    <div role="region" aria-label="Assurance">
      <h2>{lang === 'fr' ? 'Assurance' : 'Insurance'}</h2>
      {/* Affichage contrats, sinistres, plugins, etc. */}
      {plugin && plugin.render && plugin.render()}
    </div>
  );
}

Assurance.propTypes = {
  userRole: PropTypes.string.isRequired,
  lang: PropTypes.string.isRequired,
  plugin: PropTypes.object,
};

// Tests unitaires et intégration (Jest/RTL) à placer dans __tests__/

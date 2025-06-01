// Générateur de diagrammes pour Dihya 3D/VR/AR/IA
// Sécurité, i18n, plugins, auditabilité, RGPD

/**
 * Génère un diagramme Mermaid pour l’API 3D/VR/AR/IA
 * @param {string} type - Type de diagramme (architecture, flux, sécurité, i18n, plugins)
 * @param {string} lang - Langue (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
 * @returns {string} Diagramme Mermaid prêt à l’emploi
 */
function genererDiagramme(type, lang = 'fr') {
  const templates = {
    architecture: `graph TD\n  Client -->|REST/GraphQL| API[API 3D/VR/AR/IA]\n  API -->|Sécurité| WAF[WAF]\n  API -->|i18n| I18N[i18n dynamique]\n  API -->|Plugins| PLUGINS[Plugins IA/3D/VR/AR]\n  API -->|Audit| AUDIT[Audit RGPD]\n`,
    flux: `sequenceDiagram\n  User->>API: Auth (JWT, CORS)\n  API->>DB: CRUD\n  API->>Audit: Log\n  API->>i18n: Traduction\n  API->>Plugins: Appel IA/3D\n`,
    securite: `graph LR\n  API-->|JWT| Auth[Authentification]\n  API-->|CORS| CORS[CORS]\n  API-->|WAF| WAF[WAF]\n  API-->|Audit| Audit[Audit RGPD]\n`,
    i18n: `graph TD\n  API-->|fr, en, ar...| I18N[i18n dynamique]\n  I18N-->|Fallback| Fallback[Fallback IA]\n`,
    plugins: `graph TD\n  API-->|Install| Plugins[Plugins IA/3D/VR/AR]\n  Plugins-->|Audit| Audit[Audit RGPD]\n`,
  };
  return templates[type] || templates.architecture;
}

module.exports = { genererDiagramme };

"use strict";
/**
 * @file sample_plugin.js
 * @module backend/components/metiers/administration_publique/sample_plugin
 * @description Exemple de plugin Administration Publique pour Dihya Coding (audit, i18n, RGPD, extensibilité, sécurité, hooks).
 * @author Dihya Team
 * @license AGPL-3.0
 */

export default {
  name: 'SampleAdminPlugin',
  description: {
    fr: 'Plugin exemple pour Administration Publique (audit, RGPD, logs, hooks)',
    en: 'Sample plugin for Public Administration (audit, RGPD, logs, hooks)'
  },
  hooks: {
    beforeCreate: async (service, req) => {
      // Exemple : enrichir le service avec une métadonnée plugin
      service.pluginNote = 'Ajouté par SampleAdminPlugin';
    },
    beforeList: async (services, req) => {
      // Exemple : filtrer ou enrichir la liste
      return services;
    },
    beforeUpdate: async (service, req) => {
      // Exemple : log ou validation supplémentaire
    },
    beforeDelete: async (service, req) => {
      // Exemple : audit RGPD avant suppression
    }
  }
};

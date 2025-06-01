"use strict";
/**
 * @file sample_plugin.js
 * @module backend/components/metiers/agriculture/sample_plugin
 * @description Exemple de plugin Agriculture pour Dihya Coding (audit, i18n, RGPD, extensibilité, sécurité, hooks).
 * @author Dihya Team
 * @license AGPL-3.0
 */

export default {
  name: 'SampleAgriculturePlugin',
  description: {
    fr: 'Plugin exemple pour Agriculture (audit, RGPD, logs, hooks)',
    en: 'Sample plugin for Agriculture (audit, RGPD, logs, hooks)'
  },
  hooks: {
    beforeCreate: async (project, req) => {
      // Exemple : enrichir le projet avec une métadonnée plugin
      project.pluginNote = 'Ajouté par SampleAgriculturePlugin';
    },
    beforeList: async (projects, req) => {
      // Exemple : filtrer ou enrichir la liste
      return projects;
    },
    beforeUpdate: async (project, req) => {
      // Exemple : log ou validation supplémentaire
    },
    beforeDelete: async (project, req) => {
      // Exemple : audit RGPD avant suppression
    }
  }
};

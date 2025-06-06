// Sample Plugin ultra avancé pour Environnement – Dihya Coding
module.exports = {
  name: 'sample-environnement-plugin',
  hooks: {
    beforeCreate: async (ctx) => {
      ctx.audit && ctx.audit.log({ event: 'plugin_before_create', ctx });
    },
    afterCreate: async (ctx) => {
      ctx.audit && ctx.audit.log({ event: 'plugin_after_create', ctx });
    },
    beforeDelete: async (ctx) => {
      ctx.audit && ctx.audit.log({ event: 'plugin_before_delete', ctx });
    },
    afterDelete: async (ctx) => {
      ctx.audit && ctx.audit.log({ event: 'plugin_after_delete', ctx });
    },
  },
  i18n: ['fr', 'en', 'ar', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es', 'amazigh'],
  audit: true,
  rgpd: true,
  extensible: true,
  multitenant: true
};

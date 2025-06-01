/**
 * Exemples de templates métiers avancés, personnalisables, multilingues, plugins, sécurité, audit, multitenancy.
 * @module templates
 */

const templates = {
  web: {
    name: {
      fr: 'Projet Web Démo',
      en: 'Web Demo Project',
      ar: 'مشروع ويب تجريبي',
      de: 'Web-Demo-Projekt',
      zh: '网页演示项目',
      ja: 'ウェブデモプロジェクト',
      ko: '웹 데모 프로젝트',
      nl: 'Web Demo Project',
      he: 'פרויקט דמו ווב',
      fa: 'پروژه وب دمو',
      hi: 'वेब डेमो प्रोजेक्ट',
      es: 'Proyecto Web Demo',
      amazigh: 'ⴰⵎⴰⵣⵉⵖ ⵏ ⵡⴻⴱ'
    },
    description: {
      fr: 'Template web sécurisé, multitenant, plugins, audit, SEO.',
      en: 'Secure web template, multitenant, plugins, audit, SEO.',
      // ...autres langues...
    },
    plugins: ['seo', 'auth', 'audit'],
    roles: ['admin', 'user', 'guest']
  },
  ia: {
    name: {
      fr: 'Projet IA Démo',
      en: 'AI Demo Project',
      // ...autres langues...
    },
    description: {
      fr: 'Template IA avec fallback open source, RGPD, audit.',
      en: 'AI template with open source fallback, GDPR, audit.',
      // ...autres langues...
    },
    plugins: ['llama', 'mixtral', 'mistral'],
    roles: ['admin', 'user']
  }
  // ...autres templates (mobile, vr, ar)...
};

module.exports = templates;

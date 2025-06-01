// Template: Ecommerce – Dihya Coding
export default function ecommerceTemplate({ lang = 'en', plugins = [] } = {}) {
  return {
    title: lang === 'fr' ? 'E-commerce' : 'Ecommerce',
    description: lang === 'fr' ? 'Gestion avancée e-commerce.' : 'Advanced ecommerce management.',
    security: true,
    gdpr: true,
    plugins,
    ci_cd_ready: true,
  };
}

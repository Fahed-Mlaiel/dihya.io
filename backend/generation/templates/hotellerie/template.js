// Template: Hotellerie – Dihya Coding
export default function hotellerieTemplate({ lang = 'en', plugins = [] } = {}) {
  return {
    title: lang === 'fr' ? 'Hôtellerie' : 'Hospitality',
    description: lang === 'fr' ? 'Gestion avancée hôtelière.' : 'Advanced hospitality management.',
    security: true,
    gdpr: true,
    plugins,
    ci_cd_ready: true,
  };
}

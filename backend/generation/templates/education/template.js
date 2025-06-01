// Template: Education – Dihya Coding
export default function educationTemplate({ lang = 'en', plugins = [] } = {}) {
  return {
    title: lang === 'fr' ? 'Éducation' : 'Education',
    description: lang === 'fr' ? 'Gestion avancée de l’éducation.' : 'Advanced education management.',
    security: true,
    gdpr: true,
    plugins,
    ci_cd_ready: true,
  };
}

// Gestion avancée de l’internationalisation (Lead Dev)
const initialState = {
  locale: 'fr',
  supportedLocales: ['fr', 'en', 'ar', 'de', 'tzm', 'kab', 'rif', 'tac', 'es', 'it', 'pl', 'ru', 'nl', 'no', 'sv', 'pt'],
};

export default function i18nStore(state = initialState, action) {
  switch (action.type) {
    case 'SET_LOCALE':
      return { ...state, locale: action.payload };
    default:
      return state;
  }
}

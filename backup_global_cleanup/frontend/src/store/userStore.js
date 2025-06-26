// Exemple de slice/module du store : gestion de l'utilisateur
// Peut être adapté à Redux, Zustand, ou Context API selon le projet

const initialState = {
  isAuthenticated: false,
  user: null,
  roles: [],
  locale: 'fr',
};

export default function userStore(state = initialState, action) {
  switch (action.type) {
    case 'LOGIN_SUCCESS':
      return { ...state, isAuthenticated: true, user: action.payload };
    case 'LOGOUT':
      return { ...state, isAuthenticated: false, user: null };
    case 'SET_LOCALE':
      return { ...state, locale: action.payload };
    default:
      return state;
  }
}

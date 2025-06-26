// Gestion avancée des rôles et permissions (Lead Dev)
const initialState = {
  roles: [],
  permissions: {},
};

export default function rolesStore(state = initialState, action) {
  switch (action.type) {
    case 'SET_ROLES':
      return { ...state, roles: action.payload };
    case 'SET_PERMISSIONS':
      return { ...state, permissions: action.payload };
    default:
      return state;
  }
}

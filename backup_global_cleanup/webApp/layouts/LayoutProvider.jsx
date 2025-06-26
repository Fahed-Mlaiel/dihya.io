import PropTypes from 'prop-types';
import { createContext, useContext } from 'react';

/**
 * LayoutContext
 * Permet de partager dynamiquement le layout courant (utile pour plugins, analytics, accessibilité, etc.)
 */
const LayoutContext = createContext({ layout: 'main' });

export function LayoutProvider({ layout, children }) {
  return (
    <LayoutContext.Provider value={{ layout }}>
      {children}
    </LayoutContext.Provider>
  );
}

LayoutProvider.propTypes = {
  layout: PropTypes.oneOf(['main', 'auth', 'dashboard']).isRequired,
  children: PropTypes.node.isRequired,
};

export function useLayout() {
  return useContext(LayoutContext);
}

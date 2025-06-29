import PropTypes from 'prop-types';
import { useEffect } from 'react';

/**
 * AuthLayout
 * Layout dédié aux pages d’authentification (login, register, forgot password).
 * Sépare l’UI publique de l’UI métier, conforme au cahier des charges, accessibilité, audit, CI/CD ready.
 */
export default function AuthLayout({ children }) {
  useEffect(() => {
    document.title = 'Authentification – Dihya.io';
    // Audit, logs, analytics, etc.
  }, []);

  return (
    <div className="auth-layout" role="main" aria-label="Zone d’authentification">
      <main className="auth-content" tabIndex={-1} aria-label="Contenu d’authentification">
        {children}
      </main>
      <footer className="auth-footer" role="contentinfo" aria-label="Pied de page auth">
        {/* Liens RGPD, accessibilité, support, version */}
      </footer>
    </div>
  );
}

AuthLayout.propTypes = {
  children: PropTypes.node.isRequired,
};

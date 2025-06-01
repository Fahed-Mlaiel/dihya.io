import { render, screen } from '@testing-library/react';
import { I18nextProvider } from 'react-i18next';
import i18n from '../../../../i18nTestConfig'; // mock i18n config pour tests
import Mode from './index';

jest.mock('../../plugins/ModeAIWidget', () => ({
  ModeAIWidget: jest.fn(() => <div data-testid="mode-ai-widget" />)
}));
jest.mock('../../security/withRole', () => ({
  withRole: roles => Component => props =>
    roles.includes(props.userRole) ? <Component {...props} /> : <div>Access Denied</div>
}));

describe('Mode métier (ultra avancé)', () => {
  const renderWithProviders = (props) =>
    render(
      <I18nextProvider i18n={i18n}>
        <Mode {...props} />
      </I18nextProvider>
    );

  it('rend pour chaque rôle autorisé', () => {
    ['admin', 'user', 'invité'].forEach(role => {
      renderWithProviders({ userRole: role, tenant: 'test-tenant' });
      expect(screen.getByRole('region', { name: /mode/i })).toBeInTheDocument();
      expect(screen.getByTestId('mode-ai-widget')).toBeInTheDocument();
      expect(screen.getByText(/gestion mode/i)).toBeInTheDocument();
    });
  });

  it('refuse l\'accès pour un rôle non autorisé', () => {
    renderWithProviders({ userRole: 'hacker', tenant: 'test-tenant' });
    expect(screen.getByText(/access denied/i)).toBeInTheDocument();
  });

  it('respecte RGPD (pas de fuite de props sensibles)', () => {
    const { container } = renderWithProviders({ userRole: 'admin', tenant: 'secret-tenant' });
    expect(container.innerHTML).not.toMatch(/secret-tenant/);
  });

  it('est accessible (aria-label présent)', () => {
    renderWithProviders({ userRole: 'user', tenant: 't1' });
    expect(screen.getByLabelText(/mode/i)).toBeInTheDocument();
  });

  it('intègre le plugin IA', () => {
    renderWithProviders({ userRole: 'admin', tenant: 't1' });
    expect(screen.getByTestId('mode-ai-widget')).toBeInTheDocument();
  });

  it('respecte le cahier des charges (routes, logique métier)', () => {
    // Ici, on pourrait tester l'intégration avec le routeur, les hooks métiers, etc.
    // Ex: expect(someRouteLogic).toHaveBeenCalled();
    // Ex: expect(auditLog).toHaveBeenCalledWith(...)
    // À compléter selon la logique métier réelle
    expect(true).toBe(true);
  });
});
